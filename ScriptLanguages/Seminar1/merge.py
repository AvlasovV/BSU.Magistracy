"""
Реализуйте функцию, которая объединяет две отсортированные после-
довательности в одну отстортированную (merge, асимптотическая сложность алгоритма – O(n)).
Программа должна корректно работать для списков (возвращать новый отсортированный спи-
сок) и кортежей (возвращать кортеж). Использовать встроенные функции сортировки и/или
слияния запрещается.
Полный балл за задачу будет выставлен только в случае отсутствия итерирования по сорти-
руемой коллекции с помощью индексов. Иначе говоря, попробуйте избегать произвольной индек-
сации и использовать только методы объектов.
Функцию назовите merge. Программу сохраните в файле merge.py.
"""


def merge(box1, box2):
    result_box = []
    a = iter(box1)
    b = iter(box2)
    flag = None
    try:
        flag = '1'
        n1 = next(a)
        flag = '2'
        n2 = next(b)
        while True:
            minimum = min(n1, n2)
            result_box.append(minimum)
            if n1 is minimum:
                flag = '1'
                n1 = next(a)
            else:
                flag = '2'
                n2 = next(b)
    except StopIteration:
        if flag == '1':
            result_box.append(n2)
        elif flag == '2':
            result_box.append(n1)
        result_box.extend(a)
        result_box.extend(b)
    return result_box if type(box1) == list else tuple(result_box)  # I don't like this typization, but what should I do?

print(merge([1, 2, 4], [3]))
print(merge([1, 2, 5, 8, 9, 10], [3]))
print(merge([], [1, 2, 3]))
print(merge([1, 2, 3], []))