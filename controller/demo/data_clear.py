import pandas as pd  # This is the standard

# Reading a csv into Pandas.
df = pd.read_csv('.\\data\\stock.csv', header=-1)
# 设置表头
df.columns = ['序号', '日期', '平均价', '昨收', '近况', '最高', '最低', '盈利比', '压力位', '支撑位',
              '70筹码低位', '70筹码高位', '70筹码集中度', '90筹码低位', '90筹码高位', '90筹码集中度',
              '热度', '总数', '热度评价', '代码', '名称', '新股民占比', '老股民占比', '市场股民占比']
df = df.drop('序号', axis=1)
print(df)

# 去除重复项
nodup = df[-df.duplicated()]

nodup = nodup[['日期', '名称', '代码', '平均价', '昨收', '近况', '最高', '最低', '盈利比', '压力位', '支撑位',
               '70筹码低位', '70筹码高位', '70筹码集中度', '90筹码低位', '90筹码高位', '90筹码集中度',
               '热度', '总数', '热度评价', '新股民占比', '老股民占比', '市场股民占比']]

nodup.to_csv('.\\data\\clear_stock_data_1.csv')
print(nodup)
