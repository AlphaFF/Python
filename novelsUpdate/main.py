#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import pymysql
from concurrent import futures

from getter import get_novel, get_novel_info, get_novel_chapters, get_chapter_content
from chinese_digit import getResultForDigit

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


def get_novels(cursor):
    sql = 'select id, name from novels'
    cursor.execute(sql)
    values = cursor.fetchall()
    for value in values:
        yield value


def insert_content(_id, title, content, chapter):
    try:
        sql = 'insert into chapters (title, content, chapter, novel_id) values (%s, %s, %s, %s)'
        cursor.execute(sql, (title, content, chapter, _id))
    except Exception as e:
        print(e)


def download_one(*args):
    _id, name = args
    novel_url = get_novel(name)
    print('novel_url:', novel_url)
    if novel_url is not None:
        name, author = get_novel_info(novel_url)
        print('name:', name, 'author:', author)
        chapters = get_novel_chapters(novel_url)
        for _ in chapters:
            title, chapter_url = _
            try:
                chapter = re.findall(r'\d{1,}', title)[0] if re.findall(r'\d{1,}', title) else getResultForDigit(title.split()[0].replace('第', '').replace('章', ''))
            except Exception as e:
                print(e)
            else:
                # print(chapter, title, chapter_url)
                content = get_chapter_content(chapter_url)
                print(content)
                # return _id, name, title, content, chapter
                # try:
                #     insert_content(_id, title, content, chapter)
                # except Exception as e:
                #     print(e)
                #     conn.rollback()
                # finally:
                #     conn.commit()


def download_many_content(cc_list):
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        to_do = []
        for _ in cc_list:
            future = executor.submit(download_one, *_)
            to_do.append(future)
        for future in futures.as_completed(to_do):
            res = future.result()
            print('res:', res)
            try:
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


def main():
    print('time:', time.time())
    novels = get_novels(cursor)
    cc_list = [novel for novel in novels]
    download_many_content(cc_list)


if __name__ == '__main__':
    conn = connect_sql()
    cursor = conn.cursor()
    # cc_list = [(novel[0], novel[1]) for novel in novels]
    # print(cc_list)
    main()
    sched = BlockingScheduler()
    sched.add_job(main, 'interval', minutes=1)
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
