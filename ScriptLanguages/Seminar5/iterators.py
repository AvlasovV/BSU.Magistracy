"""
Задание 2. (0.5 балла). Реализуйте функцию transpose, которая транспонирует iterable вло-женных iterable.
Предполагайте, что количество элементов во всех вложенных iterable одинаково.
Другими словами, транспонирует прямоугольный двухмерный массив.Воспользуйтесь функциями
из модуля itertools и built-in функциями. Использовать циклы не разрешается.
Функцию сохраните в файле iterators.py.
Пример
expected = [[1, 2], [-1, 3]]
actual = transpose([[1, -1], [2, 3]])
assert  expected == list(map(list , actual))
"""


import itertools


def transpose(array):
    pass


if __name__ == "__main__":
    x = itertools.cycle('ABCD')
    print(next(x))