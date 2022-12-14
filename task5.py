"""
Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


res_array = [el for el in range(100, 1001, 2)]
res = reduce(my_func, [el for el in res_array])
print(res_array)
print(res)
