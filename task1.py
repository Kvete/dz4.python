"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, first_param, second_param, third_param = argv
print('имя скрипта', script_name)
print('выработка в часах:', first_param)
print('ставка в часах:', second_param)
print('премия:', third_param)


def salary(arg1, arg2, arg3):
    print(f'зарплата={arg1 * arg2 + arg3}')


salary(float(first_param), float(second_param), float(third_param))
