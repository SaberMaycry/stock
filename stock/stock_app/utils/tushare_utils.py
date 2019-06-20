import tushare as ts  # 导入tushare包

# 输入注册的Token
pro = ts.pro_api('e14c02137e597704d120f6e4ad209b3fae00b50e70a3701c5b54f02b')


def get_stock_list():
    """ 查询当前所有正常上市交易的股票列表 """
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # print(data)
    return data
