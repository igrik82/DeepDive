'''Функция первым элементом принимает функцию, вторым элементом итератор
возврашает единственный результат с итерируемого объекта согласно функции'''
from functools import reduce

list_1 = [2, 1, 3, 5, 4]


# Adder func
def adder(a: int, b: int) -> int:
    return a+b


print(reduce(adder, list_1))


# max func
def maximum(a: int, b: int) -> int:
    return a if a > b else b


print(maximum(1, 2))
print(reduce(maximum, list_1))
