import db_edit as dba
import plot_stock as ps

if __name__ == '__main__':
    name = '浪潮软件'
    date = '06-03'

    dba.get_clear_jetton_data(name, date)
    ps.plot_stock(name, date)
