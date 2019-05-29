from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StockDetail(Base):
    __tablename__ = 'tbl_stock_data'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    cur_date = Column('cur_date', String(20))
    stock_code = Column('stock_code', String(20))
    stock_name = Column('stock_name', String(20))
    cost_avg = Column('cost_avg', String(20))
    close_price = Column('close_price', String(20))
    price = Column('price', String(20))
    distribution_desc = Column('distribution_desc', String(20))
    max_price = Column('max_price', String(20))
    min_price = Column('min_price', String(20))
    profit_rate = Column('profit_rate', String(20))
    ylw = Column('ylw', String(20))
    zcw = Column('zcw', String(20))
    cost70_jgqj_down = Column('cost70_jgqj_down', String(20))
    cost70_jgqj_up = Column('cost70_jgqj_up', String(20))
    cost70_jzd = Column('cost70_jzd', String(20))
    cost90_jgqj_down = Column('cost90_jgqj_down', String(20))
    cost90_jgqj_up = Column('cost90_jgqj_up', String(20))
    cost90_jzd = Column('cost90_jzd', String(20))
    popularity = Column('popularity', String(20))
    total_stock = Column('total_stock', String(20))
    popularity_desc = Column('popularity_desc', String(20))
    new_rate = Column('new_rate', String(20))
    old_rate = Column('old_rate', String(20))
    old_avg_rate = Column('old_avg_rate', String(20))