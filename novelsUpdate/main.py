#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import pymysql
from concurrent import futures

from getter import get_novel, get_novel_info, get_novel_chapters, get_chapter_content
from chinese_digit import getResultForDigit


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='novel.log',
                    filemode='w')

MAX_WORKERS = 20

def connect_sql(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='flask',
        charset='utf8'):
    """连接数据库"""

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db,
        charset=charset)
    return conn


def get_novels():
    sql = 'select id, name from novels;'
    cursor.execute(sql)
    values = cursor.fetchall()
    for value in values:
        yield value


def insert_content(_id, title, content, chapter):
    try:
        sql = 'insert into chapters (title, content, chapter, novel_id) values (%s, %s, %s, %s)'
        cursor.execute(sql, (title, content, chapter, _id))
        conn.commit()
    except Exception as e:
        logging.info(e)
        conn.rollback()


def get_ids(novel_id):
    sql = 'select chapter from chapters where novel_id = {}'.format(novel_id)
    cursor.execute(sql)
    chapters = cursor.fetchall()
    all_chapters = []
    for chapter in chapters:
        all_chapters.append(chapter[0])
    # print(all_chapters)
    return all_chapters


def download_one(args):
    _id, name = args
    all_chapters = get_ids(_id)
    novel_url = get_novel(name)
    logging.info(novel_url)
    if novel_url is not None:
        name, author = get_novel_info(novel_url)
        # print('name:', name, 'author:', author)
        chapters = get_novel_chapters(novel_url)
        for _ in chapters:
            title, chapter_url = _
            try:
                chapter = re.findall(r'\d{1,}', title)[0] if re.findall(r'\d{1,}', title) else getResultForDigit(title.split()[0].replace('第', '').replace('章', ''))
            except Exception as e:
                logging.info(e)
            else:
                # print(chapter, title, chapter_url)
                if int(chapter) not in all_chapters:
                    content = get_chapter_content(chapter_url)
                    insert_content(_id, title, content, chapter)


def download_many_content(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, cc_list)


def main():
    global conn, cursor
    conn = connect_sql()
    cursor = conn.cursor()
    try:
        novels = get_novels()
        # cc_list = [novel for novel in novels]
        download_many_content(novels)
        cursor.close()
        conn.close()
    except Exception as e:
        logging.info(e)


if __name__ == '__main__':
    # cc_list = [(novel[0], novel[1]) for novel in novels]
    # print(cc_list)
    # get_ids(27)
    main()
    sched = BlockingScheduler()
    sched.add_job(main, 'interval', minutes=30)
    sched.start()
    # for novel in novels:
    #     print(novel)
    #     _id, name = novel
    # # get_content('龙王传说')
    #     contents = get_content(_id, name)
        # try:
        #     for content in contents:
        #         _id, name, title, content, chapter = content
        #         insert_content(_id, title, content, chapter)
        #     conn.commit()
        # except Exception as e:
        #     conn.rollback()
        # finally:
        #     conn.close()
