from utils import file_utils as fu, tushare_utils as tu

from datetime import datetime

import stock_detail_save_db as sdsd
import pandas as pd  # This is the standard


def read_csv(name):
    """ 读取csv文件 """
    data = pd.read_csv(name, header=1)
    return data


def save_stock_list():
    """更新股票列表"""
    # 设置存放股票列表路径
    stock_list_path = './/data//'

    # 判断路径是否存在，否则创建
    fu.path_exists(stock_list_path)

    # 拼接股票列表文件存放文件名
    stock_list_name = stock_list_path + datetime.now().strftime("%Y-%m-%d-%p") + '.csv'

    # 获取股票列表
    stock_list = tu.get_stock_list()

    # 股票列表写文件
    print('股票列表写文件', stock_list_name)
    stock_list.to_csv(stock_list_name)

    code_list = stock_list.symbol
    name_list = stock_list.name

    for i in range(len(code_list)):
        code = code_list[i]
        name = name_list[i]
        sdsd.save_data_to_db(code)
        print('写入', name, code)
