from datetime import datetime as dt
from datetime import date as dat


def operation_logger(val_1, op_type, val_2, res):
    time = dt.now().strftime('%H:%M')
    date = dat.today()
    with open('log.csv', 'a') as file:
        file.write('{} {} | {} {} {} = {};\n'.format(date, time, val_1, op_type, val_2, res))