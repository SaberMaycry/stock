import sys

from controller.stock import stock_list_update as slu

from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

sys.path.append('stock')  # 引入路劲


def job():
    """ 定时任务 """
    slu.save_stock_list()
    print("任务时间：", datetime.now())


def start_timer_job():
    try:
        # 定时任务
        scheduler = BlockingScheduler()
        trigger = CronTrigger(day_of_week='tue-sat',  # 周二到周六
                              hour='6',  # 每天早上6点，晚上8点
                              # hour='6,20',  # 每天早上6点，晚上8点
                              # minute='0-59', # 每分钟
                              # second='*/2' # 每隔两秒
                              )
        scheduler.add_job(job, trigger)  # 工作日上午09：30~10：00
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    except Exception as ex:
        print('发生异常：', ex)
        scheduler.shutdown()


if __name__ == '__main__':
    # start_timer_job()
    job()
