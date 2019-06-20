import datetime


def get_n_day_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    return before_n_days


def get_n_month_day_list(n):
    before_n_days = []
    for i in range(1, n + 1)[::-1]:
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i))[5:])
    return before_n_days


def get_n_month_day_list1(n):
    before_n_days = []
    for i in range(1, n + 1):
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i))[5:])
    return before_n_days


a = get_n_month_day_list(7)
print(a)

b = get_n_month_day_list1(7)
print(b)
