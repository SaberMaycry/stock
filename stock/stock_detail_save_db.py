import json
import sys
import time
import random
import requests
from utils import db_utils as db

def get_flush_data(code):
    """ 获取同花顺数据 """
    page = ''
    while page == '':
        try:
            url = 'https://basic.10jqka.com.cn/api/stockph/research/' + code + '/stock/'

            headers = {
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                'Accept-Encoding': "gzip, deflate, br",
                'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
                'Cache-control': "max-age=0",
                'Connection': "close",
                'Host': "basic.10jqka.com.cn",
                'Upgrade-Insecure-Requests': "1",
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
            }

            page = requests.request("GET", url, headers=headers)
            sleep_random(100, 200)  # 程序休眠100~200毫秒
            return json.loads(page.text)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            print("Unexpected error:", sys.exc_info())
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue


def parse_data(data):
    """ 解析同花顺股票数据，并将部分数据写入数据库 """
    status_code = data['status_code']
    status_msg = data['status_msg']

    if status_code == 0 and status_msg == 'ok':
        data = data['data']  # 数据
        user_action = data['user_action']  # 用户行为
        distribution = user_action['distribution']  # 分布数据

        stock_code = user_action['stockcode']  # 代码
        stock_name = user_action['stockname']  # 名称

        cost_avg = distribution['cost_avg']  # 平均价格
        close_price = distribution['close_price']  # 昨收
        distribution_desc = distribution['desc']  # 筹码分布描述

        max_price = distribution['max_price']  # 最高价
        min_price = distribution['min_price']  # 最低价
        profit_rate = distribution['profit_rate']  # 盈利比

        ylw = distribution['ylw']  # 压力位
        zcw = distribution['zcw']  # 支持位

        cost70_jgqj_down = distribution['cost70_jgqj_down']  # 70%筹码区间低位
        cost70_jgqj_up = distribution['cost70_jgqj_up']  # 70%筹码区间高位
        cost70_jzd = distribution['cost70_jzd']  # 70%筹码区间集中度

        cost90_jgqj_down = distribution['cost90_jgqj_down']  # 90%筹码区间低位
        cost90_jgqj_up = distribution['cost90_jgqj_up']  # 90%筹码区间高位
        cost90_jzd = distribution['cost90_jzd']  # 90%筹码区间集中度

        jeton_list = distribution['jeton_list']  # 筹码表
        jeton = jeton_list['jeton']  # 筹码列表
        price = jeton_list['price']  # 筹码价格表

        invest_data = user_action['invest_data']  # 投资理念数据
        invest_list = invest_data['data']  # 投资理念列表
        invest_desc = invest_data['desc']  # 投资理念描述

        popularity_data = user_action['popularity_data']  # 人气数据

        popularity = popularity_data['popularity']  # 人气排名
        total_stock = popularity_data['total_stock']  # 股票总数
        popularity_desc = popularity_data['desc']  # 人气描述

        date = popularity_data['date']  # 近七天交易日期
        change = popularity_data['change']  # 近七天 排名变化
        rank = popularity_data['rank']  # 近七天 排名
        total = popularity_data['total']  # 近七天股票总数

        cur_date = date[len(date) - 1]

        db.insert_popularity_data(stock_code, stock_name, date, change, rank, total)
        db.insert_jeton_list(stock_code, stock_name, cur_date, jeton_list)

        user_age_data = user_action['user_age_data']  # 股龄分布
        is_low = user_age_data['is_low']  # 是否低于市场平均老股龄 1
        new_rate = user_age_data['new_rate']  # 新股民占比
        old_rate = user_age_data['old_rate']  # 老股民占比
        old_avg_rate = user_age_data['new_rate']  # 市场个股老股民平均值

        db.insert_stock_data(cur_date, cost_avg, close_price, distribution_desc, max_price, min_price, profit_rate, ylw,
                             zcw, cost70_jgqj_down, cost70_jgqj_up, cost70_jzd, cost90_jgqj_down, cost90_jgqj_up,
                             cost90_jzd, popularity, total_stock, popularity_desc, stock_code, stock_name, new_rate,
                             old_rate, old_avg_rate)

        return cost_avg, close_price, distribution_desc, max_price, min_price, profit_rate, ylw, zcw, cost70_jgqj_down, cost70_jgqj_up, cost70_jzd, cost90_jgqj_down, cost90_jgqj_up, cost90_jzd, popularity, total_stock, popularity_desc, stock_code, stock_name, new_rate, old_rate, old_avg_rate
    else:
        print('获取数据错误！')


def random_range(start, end):
    """ 生成start~end之间的随机值 """
    return random.randint(start, end)


def sleep_random(start, end):
    """ 程序休眠随机数毫秒 """
    # 每次循环开始前,程序休眠0~1000毫秒
    time_sleep = random_range(start, end) * 0.001
    # printLog("程序休眠", time_sleep, "毫秒")
    time.sleep(time_sleep)
    # printLog("程序休眠", time_sleep, "毫秒后，程序再次启动")


def save_data_to_db(stock_code):
    """ 将解析数据写入数据库 """
    data = get_flush_data(stock_code)
    parse_data(data)
