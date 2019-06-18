from pylab import mpl
import pandas as pd  # This is the standard
import matplotlib.pyplot as plt

import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def plot_data(x_data, y_data, x_label, y_label, title):
    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.show()


def plot_jetton_stock(name, date):
    jetton_file_path = 'data/jetton/{0}/{1}{2}.csv'.format(name, name, date)

    # print(jetton_file_path)

    df_jetton = pd.read_csv(open(jetton_file_path, encoding='utf-8'), header=1)

    df_jetton.columns = ['id', 'date', 'name', 'code', 'jeton', 'price', 'percentage']

    # df_jetton.query('percentage>20 & age<40')
    # query = df_jetton.query('percentage>1')
    # query = df_jetton.query('percentage>0.5')
    # query = df_jetton.query('percentage>0.1')
    # print(query)

    # 类型转换
    df_jetton.price = df_jetton.price.astype(float)
    df_jetton.jeton = df_jetton.jeton.astype(float)

    plt.plot(df_jetton.price, df_jetton.jeton)
    plt.xlabel('股价')
    plt.ylabel('筹码')
    plt.title("{0}{1} 筹码分布".format(name, date))

    plt.show()

    # np_price = np.asarray(df_jetton.price)
    # np_jeton = np.asarray(df_jetton.jeton)
    #
    # plt.bar(np_price, np_jeton, align='center')
    #
    # plt.title('筹码')
    # plt.xlabel('股价')
    # plt.ylabel('筹码量')
    # plt.show()


def plot_popularity_stock(name, date):
    popularity_file_path = 'data/popularity/{0}/{1}{2}.csv'.format(name, name, date)

    # print(popularity_file_path)

    df_popularity = pd.read_csv(open(popularity_file_path, encoding='utf-8'), header=1)
    df_popularity.columns = ['id', 'date', 'name', 'code', 'diff', 'ranking', 'total']

    popularity_date = df_popularity.date
    # 类型转换
    popularity_ranking = np.asarray(df_popularity.ranking.astype(float))

    plt.plot(popularity_date, popularity_ranking)

    plt.xlabel('日期')
    plt.ylabel('排名')
    plt.title("{0}{1} 热度排名".format(name, date))

    plt.show()
