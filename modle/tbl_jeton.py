from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Jetton(Base):
    __tablename__ = 'tbl_jeton'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    date = Column('date', String(20))
    name = Column('name', String(20))
    code = Column('code', String(20))
    jeton = Column('jeton', String(20))
    price = Column('price', String(20))
