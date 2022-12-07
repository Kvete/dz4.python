"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим
очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция
отвечает за получение факториала числа, а в цикле необходимо выводить только
первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
n = int(input('give me n: '))


def fact(n):
    for el in range(1, n + 1):
        yield el


res = 1
for el in fact(n):
    res *= el
    print({el: res})
