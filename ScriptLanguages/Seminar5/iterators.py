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

Задание 3. (1 балл). Реализуйте функцию scalar_product, которая считает скалярное произведение
двух iterable.
Элементы могут иметь тип int или float, а также быть строками. Строки могут быть либо
представлением целых чисел (в том числе в двоичной или шестнадцатиричной системе счисления
– используйте built-in функцию int), либо состоять из букв. Обработайте этот случай с помощью
исключений, результатом вычисления в таком случае считайте None.
Воспользуйтесь функциями из модуля itertools и built-in функциями. Использовать циклы
не разрешается.
Функцию сохраните в файле iterators.py.
Пример
expected = 1
actual = scalar_product ([1 , ’2’], [-1 , 1])
assert expected == actual
actual = scalar_product ([1 , ’abc ’], [-1 , 1])
assert actual is None
"""


import itertools


def transpose(array):
    x = itertools.chain(array)
    x = list(zip(*x))
    x = list(map(list, x))
    return x


def scalar_product(ar1, ar2):
    try:
        ar1 = list(map(lambda a: a if isinstance(a, (int, float)) else int(a), ar1))
        ar2 = list(map(lambda a: a if isinstance(a, (int, float)) else int(a), ar2))
        x = list(map(lambda a, b: a * b, ar1, ar2))
        x = sum(x)
        return x
    except ValueError:
        pass
    return None



if __name__ == "__main__":

    x = [[1, 2], [-1, 3], [5, 6]]
    y, z = [1, '0', '4'], [-1, 1, 8]

    # x = itertools.chain(x)
    # print(list(zip(*x)))
    # print(list(itertools.chain.from_iterable(x)))
    # print(itertools.chain.from_iterable(x))

    # print(transpose(x))
    # print(scalar_product(y, z))
    # k = list(map(lambda a, b: a * b, z, y))
    k = scalar_product(y, z)
    # for i in k:
    #     print(list(i))
    print(k)
    print(y)