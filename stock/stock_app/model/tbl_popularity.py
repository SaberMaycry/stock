from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Popularity(Base):
    __tablename__ = 'tbl_popularity'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    date = Column('date', String(20))
    name = Column('name', String(20))
    code = Column('code', String(20))
    diff = Column('diff', String(20))
    ranking = Column('ranking', String(20))
    total = Column('total', String(20))
