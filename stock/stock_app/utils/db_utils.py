import pymysql
import sys


def create_tables(tbl_name, tbl_sql):
    """创建MySql数据表"""
    # 打开数据库连接
    db = pymysql.connect(host='localhost', port=3306, user='root', password='qqq111', db='stock', charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    try:
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        drop_tbl_sql = 'DROP TABLE IF EXISTS ' + tbl_name
        cursor.execute(drop_tbl_sql)

        # 使用预处理语句创建表
        cursor.execute(tbl_sql)
        # 关闭数据库连接
        db.close()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("如果发生错误则回滚：", sys.exc_info())
        # 关闭游标　
        cursor.close()
        # 关闭数据库连接
        db.close()


def create_tbl_popularity():
    """ 创建股票关注度表 """
    # 使用预处理语句创建表
    sql = """CREATE TABLE tbl_popularity (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                date  CHAR(20) NOT NULL,
                name  CHAR(20) NOT NULL,
                code  CHAR(20) NOT NULL,
                diff  CHAR(20) NOT NULL,
                ranking  CHAR(20) NOT NULL,
                total  CHAR(20)  NOT NULL)"""
    create_tables('tbl_popularity', sql)


def create_tbl_jeton():
    """ 创建股票筹码分布表 """
    # 使用预处理语句创建表
    sql = """CREATE TABLE tbl_jeton (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            date  CHAR(20) NOT NULL,
            name  CHAR(20) NOT NULL,
            code  CHAR(20) NOT NULL,
            jeton TEXT(20) NOT NULL,
            price TEXT(20) NOT NULL)"""
    create_tables('tbl_jeton', sql)


def create_tbl_stock_data():
    """ 创建股票筹码分布表 """
    # 使用预处理语句创建表
    sql = """CREATE TABLE tbl_stock_data (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                cur_date  TEXT(20) NOT NULL,
                cost_avg  TEXT(20) NOT NULL,
                close_price  TEXT(20) NOT NULL,
                distribution_desc TEXT(20) NOT NULL,
                max_price  TEXT(20) NOT NULL,
                min_price  TEXT(20) NOT NULL,
                profit_rate  TEXT(20) NOT NULL,
                ylw  TEXT(20) NOT NULL,
                zcw  TEXT(20) NOT NULL,
                cost70_jgqj_down  TEXT(20) NOT NULL,
                cost70_jgqj_up  TEXT(20) NOT NULL,
                cost70_jzd  TEXT(20) NOT NULL,
                cost90_jgqj_down  TEXT(20) NOT NULL,
                cost90_jgqj_up  TEXT(20) NOT NULL,
                cost90_jzd  TEXT(20) NOT NULL,
                popularity  TEXT(20) NOT NULL,
                total_stock  TEXT(20) NOT NULL,
                popularity_desc  TEXT(20) NOT NULL,
                stock_code  TEXT(20) NOT NULL,
                stock_name  TEXT(20) NOT NULL,
                new_rate  TEXT(20) NOT NULL,
                old_rate  TEXT(20) NOT NULL,
                old_avg_rate  TEXT(20) NOT NULL)"""
    create_tables('tbl_stock_data', sql)


def insert_popularity_data(stock_code, stock_name, date, change, rank, total):
    # 打开数据库连接
    db = pymysql.connect(host='localhost', port=3306, user='root', password='qqq111', db='stock', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    for i in range(len(date)):
        cur_date, name, code, diff, cur_rank, cur_total = date[i], stock_name, stock_code, change[i], rank[i], total[i]
        # sql语句
        sql = "insert into tbl_popularity values (0,%s,%s,%s,%s,%s,%s)"
        # 参数化方式传参，执行sql语句
        cursor.execute(sql, [cur_date, name, code, diff, cur_rank, cur_total])
    try:
        # 统一提交
        db.commit()
        # 关闭游标　
        cursor.close()
        # 关闭数据库连接
        db.close()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("如果发生错误则回滚：", sys.exc_info())
        # 关闭游标　
        cursor.close()
        # 关闭数据库连接
        db.close()


def insert_jeton_list(stock_code, stock_name, cur_date, jeton_list):
    jeton = jeton_list['jeton']  # 筹码列表
    price = jeton_list['price']  # 筹码价格表

    # 打开数据库连接
    db = pymysql.connect(host='localhost', port=3306, user='root', password='qqq111', db='stock', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    for i in range(len(jeton)):
        cur_date, name, code, cur_jeton, cur_price = cur_date, stock_name, stock_code, jeton[
            i], price[i]
        # sql语句
        sql = "insert into tbl_jeton values (0,%s,%s,%s,%s,%s)"
        # 参数化方式传参，执行sql语句
        cursor.execute(sql, [cur_date, name, code, cur_jeton, cur_price])
    try:
        # 统一提交
        db.commit()
        # 关闭游标　
        cursor.close()
        # 关闭数据库连接
        db.close()
    except:
        # 如果发生错误则回滚
        # db.rollback()
        print("如果发生错误则回滚：", sys.exc_info())
        # 关闭游标　
        cursor.close()
        # 关闭数据库连接
        db.close()


def insert_stock_data(cur_date, cost_avg, close_price, distribution_desc, max_price, min_price, profit_rate, ylw, zcw,
                      cost70_jgqj_down, cost70_jgqj_up, cost70_jzd, cost90_jgqj_down, cost90_jgqj_up, cost90_jzd,
                      popularity, total_stock, popularity_desc, stock_code, stock_name, new_rate, old_rate,
                      old_avg_rate):
    # 打开数据库连接
    db = pymysql.connect(host='localhost', port=3306, user='root', password='qqq111', db='stock', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO tbl_stock_data(cur_date, cost_avg, close_price, distribution_desc, max_price, min_price, profit_rate, ylw, zcw, cost70_jgqj_down, cost70_jgqj_up, cost70_jzd, cost90_jgqj_down, cost90_jgqj_up, cost90_jzd, popularity, total_stock, popularity_desc, stock_code, stock_name, new_rate, old_rate, old_avg_rate) VALUES ('{0}','{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}', '{22}')""".format(
        cur_date, cost_avg, close_price, distribution_desc, max_price, min_price, profit_rate, ylw, zcw,
        cost70_jgqj_down, cost70_jgqj_up, cost70_jzd, cost90_jgqj_down, cost90_jgqj_up, cost90_jzd, popularity,
        total_stock, popularity_desc, stock_code, stock_name, new_rate, old_rate, old_avg_rate)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("如果发生错误则回滚：", sys.exc_info())
        # 关闭数据库连接
        db.close()


def reset_db():
    """ 重置数据库 """
    create_tbl_popularity()
    create_tbl_stock_data()
    create_tbl_jeton()


if __name__ == '__main__':
    reset_db()
