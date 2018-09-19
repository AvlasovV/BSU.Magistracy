"""
Напишите функцию, которая для выборки, заданной списком, и заданно-
го натурального числа k посчитает и выведет гистограмму распределения шириной k. Другими
словами, найдет максимум и минимум, поделит интервал на k частей (1 <= k <= d, d – количе-
ство различных элементов в списке) и посчитает, сколько элементов выборки попало в каждый
интервал.
Верните список длины k, содержащий количество элементов в каждой ячейке. Левую границу
интервалов считайте включая, правую – исключая (кроме последнего интервала). Желательно
реализовать алгоритм со сложностью O(n), где n – длина входного списка.
Замечание. Функцию назовите distribute. Программу сохраните в файле hist.py.

Пример
assert distribute ([1.25 , 1, 2, 1.75], 2) == [2, 2]
"""


def minmax(selection):
    """Just for best speed, because here is only one passing through list"""
    max_value = None
    min_value = None
    for value in selection:
        if not min_value:
            min_value = value
            max_value = value
        elif value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    return min_value, max_value


def distribute(selection, k):
    min, max = minmax(selection)
    diameter = max - min
    # intervals = [x for x in range(min, max, diameter / k)]
    intervals = []
    step = diameter / k
    pointer = min
    while pointer <= max:
        intervals.append(pointer)
        pointer += step
    for number in selection:
        i = int((number - min) / step) + 1

        return [min, max], intervals, step


if __name__ == '__main__':
    print((distribute([1.25, 1, 2, 1.75], 2)))