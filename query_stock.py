import db_edit as dba
import plot_stock as ps

if __name__ == '__main__':
    name = '中通客车'
    # name = '温氏股份'
    # name = '牧原股份'
    date = '06-04'
    # date = '05-31'

    dba.get_clear_jetton_data(name, date)
    ps.plot_stock(name, date)
