from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
import pandas as pd  # This is the standard
from utils import file_utils as fu

from modle.tbl_jeton import Jetton
from modle.tbl_popularity import Popularity
from modle.tbl_stock_data import StockDetail

db_name = 'stock'
# db_name = 'saber'

# mysqlclient 驱动
MYSQLDB_CONNECT_STRING = 'mysql+mysqldb://root:qqq111@localhost/' + db_name + '?charset=utf8mb4&binary_prefix=true'
# PyMySQL 驱动
PYMYSQL_CONNECT_STRING = 'mysql+pymysql://root:qqq111@localhost/' + db_name + '?charset=utf8mb4&binary_prefix=true'

# 当前日期
CURRENT_DATE = './data/' + datetime.now().strftime('%Y-%m-%d')
MONTH_DAY = datetime.now().strftime('%m-%d')


# 创建数据库引擎，选择上述引擎类型，echo为True,会打印所有的sql语句
engine = create_engine(PYMYSQL_CONNECT_STRING, echo=True)

# 创建会话类
DB_Session = sessionmaker(bind=engine)

# 创建会话对象
session = DB_Session()

# 接下来，利用session搞一些事情吧
Base = declarative_base()

# 创建表（如果表已经存在，则不会创建）
Base.metadata.create_all(engine)


def get_clear_popularity_data(name, date):
    # 查询热度记录
    popularity_list = session.query(Popularity).filter(Popularity.name == name)

    # 将热度对象列表，转化为二位数组
    arr = []
    for item in popularity_list:
        arr.append([item.id, item.date, item.name, item.code, item.diff, item.ranking, item.total])
    # 利用二维数组生产pandas数据帧
    df = pd.DataFrame(arr, columns=['id', 'date', 'name', 'code', 'diff', 'ranking', 'total'])
    print(df)
    # 去除id列
    df = df.drop('id', axis=1)
    # 去除重复项
    popularity_data = df[-df.duplicated()]
    print(popularity_data)

    popularity_dir = 'data/popularity/{0}'.format(name)
    fu.path_exists(popularity_dir)
    popularity_file_path = '{0}/{1}{2}.csv'.format(popularity_dir, name, date)
    popularity_data.to_csv(popularity_file_path)

    # 用完记得关闭，也可以用with
    session.close()


def get_clear_jetton_data(name, date):
    # 查询筹码记录

    jetton_list = session.query(Jetton).filter(Jetton.name == name, Jetton.date == date)
    # 将热度对象列表，转化为二位数组
    arr = []
    for item in jetton_list:
        arr.append([item.date, item.name, item.code, float(item.jeton), float(item.price)])
    # 利用二维数组生产pandas数据帧
    df = pd.DataFrame(arr, columns=['date', 'name', 'code', 'jeton', 'price'])
    # 去除重复项
    jetton_data = df[-df.duplicated()]

    # 筹码总和
    jetton_total = 0
    for index, row in jetton_data.iterrows():
        jetton = jetton_data.jeton[index]
        price = jetton_data.price[index]
        jetton_total += jetton * price

    # 百分比
    percentage_list = []
    for index, row in jetton_data.iterrows():
        jetton = row['jeton']
        price = row['price']
        percentage = jetton * price / jetton_total * 100
        percentage_list.append(percentage)

    # 添加百分比列
    jetton_data['percentage'] = percentage_list

    temp_dir = 'data/jetton/{0}'.format(name)
    fu.path_exists(temp_dir)
    jetton_file_path = '{0}/{1}{2}.csv'.format(temp_dir, name, date)
    jetton_data.to_csv(jetton_file_path)

    # # 用完记得关闭，也可以用with
    session.close()


def get_clear_stock_data(name, date):
    # 查询股票详情记录
    stock_detail_list = session.query(StockDetail).filter(StockDetail.name == name, StockDetail.date == date)

    # 将热度对象列表，转化为二位数组
    arr = []
    for item in stock_detail_list:
        arr.append([item.id, item.date, item.name, item.code, item.diff, item.ranking, item.total])
    # 利用二维数组生产pandas数据帧
    df = pd.DataFrame(arr, columns=['id', 'date', 'name', 'code', 'diff', 'ranking', 'total'])
    print(df)
    # 去除id列
    df = df.drop('id', axis=1)
    # 去除重复项
    popularity_data = df[-df.duplicated()]
    print(popularity_data)
    
    detail_dir = 'data/detail/{0}'.format(name)
    fu.path_exists(detail_dir)
    detail_file_path = '{0}/{1}{2}.csv'.format(detail_dir, name, date)

    popularity_data.to_csv(detail_file_path)

    # session.add_all()
    # 用完记得关闭，也可以用with
    session.close()