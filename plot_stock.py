from pylab import mpl
import pandas as pd  # This is the standard
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# file_name = '亚星客车'
# file_name = '中通客车'
# file_name = '广和通'
# file_name = '新国都'


def plot_stock(name, date):
    jetton_file_path = 'data/jetton/{0}{1}.csv'.format(name, date)

    df_jetton = pd.read_csv(jetton_file_path, header=1)

    df_jetton.columns = ['id', 'date', 'name', 'code', 'jeton', 'price', 'percentage']
    # print(df_jetton)

    # df_jetton.query('percentage>20 & age<40')
    # query = df_jetton.query('percentage>1')
    # query = df_jetton.query('percentage>0.5')
    # query = df_jetton.query('percentage>0.1')
    # print(query)
    print(df_jetton)

    # 类型转换
    df_jetton.price = df_jetton.price.astype(float)
    df_jetton.jeton = df_jetton.jeton.astype(float)

    df_jetton.plot(x='price', y=['jeton'])
    plt.xlabel('股价')
    plt.ylabel('筹码')
    plt.title("{0}{1} 筹码分布".format(name, date))

    plt.show()


if __name__ == '__main__':
    name = '中通客车'
    date = '06-03'

    plot_stock(name, date)
