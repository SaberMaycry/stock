from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# sql = """CREATE TABLE tbl_jeton (
#         id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#         date  CHAR(20) NOT NULL,
#         name  CHAR(20) NOT NULL,
#         code  CHAR(20) NOT NULL,
#         jeton TEXT(20) NOT NULL,
#         price TEXT(20) NOT NULL)"""

class Jetton(Base):
    __tablename__ = 'tbl_jeton_temp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(20))
    name = Column(String(20))
    code = Column(String(20))
    jeton = Column(String(20))
    price = Column(String(20))

    def __repr__(self):
        return "<Jetton(id='%d', date='%s', name='%s', code='%s', jeton='%s', price='%s')>" % (
            self.id, self.date, self.name, self.code, self.jeton, self.price)


# mysqlclient 驱动
engine = create_engine("mysql+mysqldb://root:qqq111@localhost/stock?charset=utf8mb4&binary_prefix=true",
                       pool_recycle=3600, echo=True)

# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

db_jetton = Jetton(date='05-17', name='浦发银行', code='600000', jeton='2780191.10626279', price='9.62')
add = session.add(db_jetton)
session.commit()

# session.rollback()
# print('----------------------------------------------------------')
# for item in session.query(Jetton).order_by(Jetton.id):
#     print(item.id, item.name, item.price)

# for item in session.query(Jetton).order_by(Jetton.id):
#     print(item.id, item.name, item.price)
# print('----------------------------------------------------------')
# for row in session.query(Jetton, Jetton.name).all():
#     print(row.Jetton, row.name)

query = session.query(Jetton)

for item in query:
    print(item)

# print(query)
