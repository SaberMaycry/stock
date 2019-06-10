import pandas as pd  # This is the standard
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

df = pd.read_csv('.\\data\\clear_stock_data_1.csv', header=-1)
# print(df)
df.columns = ['序号', '日期', '名称', '代码', '平均价', '昨收', '近况', '最高', '最低', '盈利比', '压力位', '支撑位',
              '70低位', '70高位', '70集中度', '90低位', '90高位', '90集中度',
              '热度', '总数', '热度评价', '新股民', '老股民', '市场股民']

stock_name = '牧原股份'  # 广和通 亚星客车 中通客车

ght_df = df[(df['名称'] == stock_name)]

ght_df = ght_df.drop(['序号', '名称', '代码', '近况', '最高', '最低', '盈利比',
                      '70低位', '70高位', '70集中度', '90低位', '90高位', '90集中度',
                      '总数', '热度评价', '新股民', '老股民', '市场股民'], axis=1)

ght_df.columns = ['date', 'average', 'close', 'ylw', 'zcw', 'popularity']

# 类型转换
ght_df[["average"]] = ght_df[["average"]].astype(float)
ght_df[["close"]] = ght_df[["close"]].astype(float)
ght_df[["ylw"]] = ght_df[["ylw"]].astype(float)
ght_df[["zcw"]] = ght_df[["zcw"]].astype(float)
ght_df[["popularity"]] = ght_df[["popularity"]].astype(float)

print(ght_df)

ght_df.plot(x='date', y=['average', 'close', 'ylw', 'zcw'])
plt.xlabel('日期')
plt.ylabel('股价')
plt.title(stock_name)

ght_df.plot(x='date', y=['popularity'])
plt.xlabel('日期')
plt.ylabel('热度')
plt.title(stock_name)

plt.show()
