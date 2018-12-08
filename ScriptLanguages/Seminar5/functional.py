"""
Задание 1. Напишите функцию, которая при каждом вызове возвращает количе-ство раз, которое она была вызвана.
Использовать глобальные переменные не допускается, иначеговоря, в файле должно быть
только определение функции (с ключевым словом def).
Замечание.Функцию назовите smart_function. Программу сохраните в файлеfunctional.py.
Пример
for  real_call_count  in  xrange(1, 5):
    assert f() == real_call_count

Задание 4. (1 балл). Реализуйте функцию-генератор flatten, которая разворачивает вложенные
итерируемые объекты в один iterable.
Обратите внимание, что строки, хоть они и являются итерируемыми, распаковывать не нужно.
Рекурсивно вызывать функцию не следует. Преобразовывать итерируемые объекты к спискам
запрещено.
Функцию сохраните в файле functional.py.
Пример
expected = [1 , 2 , 0 , 1 , 1 , 2 , 1 , ’ab ’]
actual = flatten ([1 , 2 , xrange ( 2 ) , [[], [1], [[2]]], ( x for x in [1]) , ’ab ’])
assert expected == list ( actual )

"""


def smart_function():
    if hasattr(smart_function, "count"):
        smart_function.count += 1
    else:
        smart_function.count = 1
    return smart_function.count


def flatten(args):
    for elem in args:
        if hasattr(elem, "__iter__") and not isinstance(elem, (str, bytes)):
            yield from flatten(elem)
        else:
            yield elem


if __name__ == "__main__":

    # for i in range(10):
    #     print(smart_function())

    for real_call_count in range(1, 5):
        assert smart_function() == real_call_count

    expected = [1, 2, 0, 1, 1, 2, 1, 'ab']
    actual = list(flatten([1, 2, range(2), [[], [1], [[2]]], (x for x in [1]), 'ab']))
    print(list(actual))
    assert expected == list(actual)