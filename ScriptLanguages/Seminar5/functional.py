"""
Задание 1. Напишите функцию, которая при каждом вызове возвращает количе-ство раз, которое она была вызвана.
Использовать глобальные переменные не допускается, иначеговоря, в файле должно быть
только определение функции (с ключевым словом def).
Замечание.Функцию назовите smart_function. Программу сохраните в файлеfunctional.py.
Пример
for  real_call_count  in  xrange(1, 5):
    assert f() == real_call_count
"""


def smart_function():
    if hasattr(smart_function, "count"):
        smart_function.count += 1
    else:
        smart_function.count = 1
    return smart_function.count


if __name__ == "__main__":

    # for i in range(10):
    #     print(smart_function())

    for real_call_count in range(1, 5):
        assert smart_function() == real_call_count