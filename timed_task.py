#!/usr/bin/env python3
# coding=utf-8

"""
python定时任务:
1. 使用time.sleep
2. 使用threading模块中的Timer
3. 使用sched模块
4. 使用APScheduler定时框架
"""


from datetime import datetime, timedelta
import sched
import time
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler
# # 使用time.sleep
# # 只能执行固定间隔时间的任务，如果有定时任务就无法完成，比如早上六点半喊我起床。
# # 并且 sleep 是一个阻塞函数，也就是说 sleep 这一段时间，啥都不能做
# def timer(n):
#     while n < 5:
#         print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         time.sleep(n)
#         n += 1


# timer(0)


# 使用threading模块中的Timer
# # Timer 函数第一个参数是时间间隔（单位是秒），第二个参数是要调用的函数名，第三个参数是调用函数的参数(tuple)
# def printTime(inc):
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     t = Timer(inc, printTime, (inc, ))
#     t.start()


# printTime(2)


# # 使用sched模块
# # 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
# schedule = sched.scheduler(time.time, time.sleep)


# # 被周期性调度触发的函数
# def printTime(inc):
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     schedule.enter(inc, 0, printTime, (inc, ))


# # enter四个参数分别为：间隔时间、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
# # 给该触发函数的参数（tuple形式）
# def main(inc=2):
#     schedule.enter(0, 0, printTime, (inc, ))
#     # 注意 sched 模块不是循环的，一次调度被执行后就 Over 了，如果想再执行，请再次 enter
#     schedule.run()


# main()


# 使用APScheduler定时框架
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# BlockingScheduler 和 BackgroundScheduler，当调度器是应用中唯一要运行的任务时，
# 使用 BlockingSchedule，如果希望调度器在后台执行，使用 BackgroundScheduler
scheduler = BlockingScheduler()
# cron: crontab类型任务
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)

# interval: 固定时间间隔任务
# sched.add_job(job, 'interval', seconds=5)

# date: 基于日期时间的一次性任务
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# scheduler.add_job(job, next_run_time=(datetime.now() + timedelta(seconds=3)))
scheduler.start()

