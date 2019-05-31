from pylab import mpl
import pandas as pd  # This is the standard
import matplotlib.pyplot as plt

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

file_name = '05-30'

df_jetton = pd.read_csv('sqlalchemy\\data\\jetton\\' + file_name + '.csv', header=1)

df_jetton.columns = ['id', 'date', 'name', 'code', 'jeton', 'price', 'percentage']
print(df_jetton)

# 类型转换
df_jetton.price = df_jetton.price.astype(float)
df_jetton.jeton = df_jetton.jeton.astype(float)

df_jetton.plot(x='price', y=['jeton'])
plt.xlabel('股价')
plt.ylabel('筹码')
plt.title("广和通 {0} 筹码分布".format(file_name))

plt.show()
