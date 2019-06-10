from pylab import mpl
import pandas as pd  # This is the standard
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def plot_stock(name, date):
    jetton_file_path = 'data/jetton/{0}/{1}{2}.csv'.format(name, name, date)

    print(jetton_file_path)
    
    df_jetton = pd.read_csv(open(jetton_file_path,encoding='utf-8'), header=1)

    df_jetton.columns = ['id', 'date', 'name', 'code', 'jeton', 'price', 'percentage']
    # print(df_jetton)

    # df_jetton.query('percentage>20 & age<40')
    query = df_jetton.query('percentage>1')
    # query = df_jetton.query('percentage>0.5')
    # query = df_jetton.query('percentage>0.1')
    print(query)
    # print(df_jetton)

    # 类型转换
    df_jetton.price = df_jetton.price.astype(float)
    df_jetton.jeton = df_jetton.jeton.astype(float)

    df_jetton.plot(x='price', y=['jeton'])
    plt.xlabel('股价')
    plt.ylabel('筹码')
    plt.title("{0}{1} 筹码分布".format(name, date))

    plt.show()
