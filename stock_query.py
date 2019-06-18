from utils import sql_utils as su
from utils import plot_utils as pu
import numpy as np

if __name__ == '__main__':
    # name = '中通客车'
    # name = '温氏股份'
    # name = '牧原股份'
    # name = '中兴通讯'
    name = '亚星客车'
    # name = '新国都'
    # name = '广电网络'
    date = '06-17'
    # date = '06-06'

    # 查询筹码分布
    # jet = su.get_clear_jetton_data(name, date)
    # pu.plot_data(jet.price, jet.jeton, '股价', '筹码', '{0}{1} 筹码分布'.format(name, date))

    # 查询热度排名
    # popu = su.get_clear_popularity_data(name, date)
    # popularity_ranking = np.asarray(popu.ranking.astype(float))
    # pu.plot_data(popu.date, popularity_ranking, '日期', '热度', '{0}{1} 热度变化'.format(name, date))

    # # 查询详情信息
    detail = su.get_clear_stock_data(name, date)

    # 利用二维数组生产pandas数据帧
    # df = pd.DataFrame(arr, columns=['id', 'cur_date', 'stock_code', 'stock_name', 'cost_avg', 'close_price',
    #                                 'distribution_desc', 'max_price', 'min_price', 'profit_rate', 'ylw', 'zcw',
    #                                 'cost70_jgqj_down', 'cost70_jgqj_up', 'cost70_jzd', 'cost90_jgqj_down',
    #                                 'cost90_jgqj_up', 'cost90_jzd', 'popularity', 'total_stock', 'popularity_desc',
    #                                 'new_rate', 'old_rate', 'old_avg_rate'])
    # 去除id列
    # detail = detail.drop(
    #     ['stock_code', 'stock_name', 'close_price', 'total_stock', 'new_rate', 'old_rate', 'popularity_desc',
    #      'old_avg_rate'], axis=1)

    detail.columns = ['日期', '名称', '代码', '平均价', '昨收', '近况', '最高', '最低', '盈利比', '压力位', '支撑位',
                      '70低位', '70高位', '70集中度', '90低位', '90高位', '90集中度',
                      '热度', '总数', '热度评价', '新股民', '老股民', '市场股民']

    detail = detail.drop(['名称', '代码', '近况', '最高', '最低', '盈利比',
                          '总数', '热度评价', '新股民', '老股民', '市场股民'], axis=1)

    # ght_df.columns = ['date', 'average', 'close', 'ylw', 'zcw', 'popularity']

    for index, row in detail.iterrows():
        print(row['日期'], row['平均价'], row['昨收'], row['压力位'], row['支撑位'],
              row['70低位'], row['70高位'], row['70集中度'],
              row['90低位'], row['90高位'], row['90集中度'], row['热度'])  # 输出每行的索引值

    # for index, row in detail.iteritems():
    #     print(row)  # 输出列名
