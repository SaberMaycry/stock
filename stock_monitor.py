import csv
import random
from datetime import datetime

import requests
import wxpy as wx
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

oldPrice = 0.000
oldPercentage = 0.000

# Release
debugMode = False


# Debug
# debugMode = True


def init_wx(name):
    """ 初始化微信通讯 """
    bot = wx.Bot(cache_path=True)
    receiver = bot.search(name)[0]
    return receiver


def send_msg(msg):
    """ 发送消息 """
    receiver.send(msg)


def real_stock_data(stock_codes):
    """ 获取数据 """
    dict = {}
    for code in stock_codes:
        stockUrl = 'http://hq.sinajs.cn/list=' + code
        httpRes = requests.get(stockUrl).text
        strs = httpRes.split("\"")[1].split(",")
        jsonStr = format_data(strs)
        dict[code] = jsonStr
    return dict


def format_data(stock):
    """ 格式化数据 """
    stock_dict = dict(
        name=stock[0],
        open=float(stock[1]),
        close=float(stock[2]),
        now=float(stock[3]),
        high=float(stock[4]),
        low=float(stock[5]),
        buy=float(stock[6]),
        sell=float(stock[7]),
        turnover=int(stock[8]),
        volume=float(stock[9]),
        bid1_volume=int(stock[10]),
        bid1=float(stock[11]),
        bid2_volume=int(stock[12]),
        bid2=float(stock[13]),
        bid3_volume=int(stock[14]),
        bid3=float(stock[15]),
        bid4_volume=int(stock[16]),
        bid4=float(stock[17]),
        bid5_volume=int(stock[18]),
        bid5=float(stock[19]),
        ask1_volume=int(stock[20]),
        ask1=float(stock[21]),
        ask2_volume=int(stock[22]),
        ask2=float(stock[23]),
        ask3_volume=int(stock[24]),
        ask3=float(stock[25]),
        ask4_volume=int(stock[26]),
        ask4=float(stock[27]),
        ask5_volume=int(stock[28]),
        ask5=float(stock[29]),
        date=stock[30],
        time=stock[31],
    )
    return stock_dict


def prase_price(stockMessage, now):
    """ 解析价格 """
    global oldPrice, oldPercentage

    # 测试价格
    if debugMode:
        now = float(now) + random.randint(-9, 9) / 10

    # 两次行情不同时，才判断价格
    if oldPrice == 0.000:
        oldPrice = now
        return

    if oldPrice != now:
        # 超过额度通知
        delimit = get_delimit()

        percentage = round((now - oldPrice) / oldPrice * 100, 2)
        strPercentage = '浮动：{}%'.format(percentage) + '\n'
        if abs(percentage) >= delimit and percentage != oldPercentage:
            oldPercentage = percentage
            oldPrice = now
            send_msg(strPercentage + stockMessage)
        else:
            print(datetime.now().strftime("%H:%M:%S") + ' ' + strPercentage)


def write_csv_by_stock(stock):
    name = stock.get('name')
    buy = stock.get('buy')
    sell = stock.get('sell')
    now = stock.get('now')
    open = stock.get('open')
    close = stock.get('close')
    high = stock.get('high')
    low = stock.get('low')
    time = stock.get('time')

    headers, rows = parse_csv(stock)
    path = '.\\stock\\' + name + '\\' + datetime.now().strftime("%Y-%m-%d-%p") + '.csv'
    write_csv(headers, rows, path)

    stock_message = '时间：{}\n'.format(time) + '名称：{}\n'.format(name) + '竞买：{}\n'.format(buy) + '竞卖：{}\n'. \
        format(sell) + '当前：{}\n'.format(now) + '今开：{}\n'.format(open) + '昨收：{}\n'.format(close) + \
                    '最高：{}\n'.format(high) + '最低：{}'.format(low)

    prase_price(stock_message, now)


def job():
    """ 定时任务 """
    # stock_codes = ['sz300638','sh600776','sz000063']
    # ght = real_stock_data(stock_codes).get('sz300638')
    # dftx = real_stock_data(stock_codes).get('sh600776')

    stock_codes = [get_stock()]
    stock = real_stock_data(stock_codes).get(get_stock())

    write_csv_by_stock(stock)


def get_mockapi():
    """ 获取api数据 """
    # stockUrl = 'http://www.wanandroid.com/tools/mockapi/4852/stock'
    # httpRes = requests.get(stockUrl).text
    httpRes = '0.2&监控&sz002714'
    resList = httpRes.split('&')
    return resList


def get_delimit():
    """ 获取限定价格 """
    delimit = float(get_mockapi()[0])
    return delimit


def get_receiver():
    """ 获取接收者 """
    name = get_mockapi()[1]
    return name


def get_stock():
    """ 获取监控股票 """
    stock = get_mockapi()[2]
    return stock


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path, ' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path, ' 目录已存在')
        return False


def write_csv(headers, rows, path):
    """ 写CSV文件 """
    if mkdir(path):
        with open(path, 'a', newline='') as f:
            f_csv = csv.writer(f)
            if f.tell() == 0:
                f_csv.writerow(headers)
            f_csv.writerows(rows)


def parse_csv(stock):
    """ 解析CSV文件 """

    headers = []
    row = []

    for key in stock:
        value = str(stock[key])
        headers.append(key)
        row.append(value)

    rows = [row]
    return headers, rows


if __name__ == '__main__':
    name = get_receiver()

    receiver = init_wx(name)

    try:
        # 定时任务
        scheduler = BlockingScheduler()
        cronSecond = '*/5'
        if debugMode:
            trigger = CronTrigger(second=cronSecond)
            scheduler.add_job(job, trigger, id='debug', max_instances=10)
        else:
            trigger1 = CronTrigger(day_of_week='mon-fri', hour='9', minute='30-59', second=cronSecond)
            scheduler.add_job(job, trigger1, id='release1', max_instances=10)  # 工作日上午09：30~10：00

            trigger2 = CronTrigger(day_of_week='mon-fri', hour='10', minute='0-59', second=cronSecond)
            scheduler.add_job(job, trigger2, id='release2', max_instances=10)  # 工作日上午10：30~11：00

            trigger3 = CronTrigger(day_of_week='mon-fri', hour='11', minute='0-30', second=cronSecond)
            scheduler.add_job(job, trigger3, id='release3', max_instances=10)  # 工作日上午11：00~11：30

            trigger4 = CronTrigger(day_of_week='mon-fri', hour='13-14', minute='0-59', second=cronSecond)
            scheduler.add_job(job, trigger4, id='release4', max_instances=10)  # 工作日上午13：00~15：00
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    except Exception as ex:
        print('发生异常：', ex)
        scheduler.shutdown()
