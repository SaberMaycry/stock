from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime
import pandas as pd  # This is the standard
from utils import file_utils as fu
from tbl_jeton import Jetton
from tbl_popularity import Popularity
from tbl_stock_data import StockDetail

# mysqlclient 驱动
MYSQLDB_CONNECT_STRING = 'mysql+mysqldb://root:qqq111@localhost/saber?charset=utf8mb4&binary_prefix=true'
# PyMySQL 驱动
PYMYSQL_CONNECT_STRING = 'mysql+pymysql://root:qqq111@localhost/saber?charset=utf8mb4&binary_prefix=true'
# 当前日期
CURRENT_DATE = './data/' + datetime.now().strftime('%Y-%m-%d')
MONTH_DAY = datetime.now().strftime('%m-%d')
fu.path_exists(CURRENT_DATE)

POPULARITY_FILE_NAME = CURRENT_DATE + '/popularity.csv'
JETTON_FILE_NAME = CURRENT_DATE + '/jetton.csv'
STOCK_FILE_NAME = CURRENT_DATE + '/stock.csv'

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


def get_clear_popularity_data():
    # 查询所有热度记录
    popularity_list = session.query(Popularity)

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

    popularity_data.to_csv(POPULARITY_FILE_NAME)

    # session.add_all()
    # 用完记得关闭，也可以用with
    session.close()


def get_clear_jetton_data():
    # 查询所有热度记录
    # jetton_list = session.query(Jetton).filter(Jetton.date == MONTH_DAY, Jetton.name == '广和通')
    # jetton_list = session.query(Jetton).filter(Jetton.name == '广和通')

    temp_date = '05-20'
    temp_name = '亚星客车'

    jetton_list = session.query(Jetton).filter(Jetton.date == temp_date, Jetton.name == temp_name)
    # 将热度对象列表，转化为二位数组
    arr = []
    for item in jetton_list:
        arr.append([item.id, item.date, item.name, item.code, item.jeton, item.price])
    # 利用二维数组生产pandas数据帧
    df = pd.DataFrame(arr, columns=['id', 'date', 'name', 'code', 'jeton', 'price'])
    # 去除id列
    df = df.drop('id', axis=1)
    print('df长度：', len(df))
    # 去除重复项
    jetton_data = df[-df.duplicated()]
    print('jetton_data长度：', len(jetton_data))

    i = 0
    for index, row in jetton_data.iterrows():
        print(i, index)
        print(row["jeton"], row["price"])
        i += 1

    # # 转换类对象的数据类型
    # jetton_data['jeton'] = jetton_data['jeton'].astype(float)
    # jetton_data['price'] = jetton_data['price'].astype(float)
    #
    # # 筹码总和
    # jetton_total = 0
    #
    # jetton_len = len(jetton_data)
    #
    # for i in range(jetton_len):
    #     jetton = jetton_data.jeton[i]
    #     price = jetton_data.price[i]
    #
    #     print(i, jetton, price)
    # jetton_total += jetton * price
    #
    # percentage_list = []
    # for i in range(len(jetton_data)):
    #     jetton = jetton_data.jeton[i]
    #     price = jetton_data.price[i]
    #     # 百分比
    #     percentage = jetton * price / jetton_total * 100
    #     percentage_list.append(percentage)
    #
    # jetton_data['percentage'] = percentage_list
    #
    # print(jetton_data)
    # # jetton_data.to_csv(JETTON_FILE_NAME)
    # jetton_data.to_csv('data/jetton/' + temp_date + temp_name + '.csv')
    # # session.add_all()
    # # # 用完记得关闭，也可以用with
    # # session.close()


def get_clear_stock_data():
    # 查询所有热度记录
    stock_detail_list = session.query(StockDetail)

    # id = Column('id', Integer, primary_key=True, autoincrement=True)
    # cur_date = Column('cur_date', String(20))
    # stock_code = Column('stock_code', String(20))
    # stock_name = Column('stock_name', String(20))
    # cost_avg = Column('cost_avg', String(20))
    # close_price = Column('close_price', String(20))
    # price = Column('price', String(20))
    # distribution_desc = Column('distribution_desc', String(20))
    # max_price = Column('max_price', String(20))
    # min_price = Column('min_price', String(20))
    # profit_rate = Column('profit_rate', String(20))
    # ylw = Column('ylw', String(20))
    # zcw = Column('zcw', String(20))
    # cost70_jgqj_down = Column('cost70_jgqj_down', String(20))
    # cost70_jgqj_up = Column('cost70_jgqj_up', String(20))
    # cost70_jzd = Column('cost70_jzd', String(20))
    # cost90_jgqj_down = Column('cost90_jgqj_down', String(20))
    # cost90_jgqj_up = Column('cost90_jgqj_up', String(20))
    # cost90_jzd = Column('cost90_jzd', String(20))
    # popularity = Column('popularity', String(20))
    # total_stock = Column('total_stock', String(20))
    # popularity_desc = Column('popularity_desc', String(20))
    # new_rate = Column('new_rate', String(20))
    # old_rate = Column('old_rate', String(20))
    # old_avg_rate = Column('old_avg_rate', String(20))

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

    popularity_data.to_csv(POPULARITY_FILE_NAME)

    # session.add_all()
    # 用完记得关闭，也可以用with
    session.close()


if __name__ == '__main__':
    # get_clear_popularity_data()
    get_clear_jetton_data()
