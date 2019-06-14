from utils import sql_utils as su
from utils import plot_utils as pu

if __name__ == '__main__':
    # name = '中通客车'
    # name = '温氏股份'
    # name = '牧原股份'
    # name = '中兴通讯'
    # name = '亚星客车'
    # name = '新国都'
    name = '广电网络'
    date = '06-13'
    # date = '05-31'

    # 查询筹码分布
    su.get_clear_jetton_data(name, date)
    pu.plot_stock(name, date)

    # 查询热度排名
    su.get_clear_popularity_data(name, date)

    # 查询详情信息
    su.get_clear_stock_data(name, date)
