from utils import sql_utils as su
from utils import plot_utils as pu

if __name__ == '__main__':
    # name = '中通客车'
    # name = '温氏股份'
    name = '牧原股份'
    date = '06-06'
    # date = '05-31'

    su.get_clear_jetton_data(name, date)
    pu.plot_stock(name, date)
