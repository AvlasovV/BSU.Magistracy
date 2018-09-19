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
        if min_value is None:
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
    step = diameter / k

    hist = [0 for _ in range(k)]
    for number in selection:
        i = int((number - min) / step)
        if number == max:
            hist[k - 1] += 1
        elif (min + i * step) <= number:
            hist[i] += 1
        elif (min + i * step) == number:
            hist[i - 1] += 1
    return hist


if __name__ == '__main__':
    print((distribute([1.25, 1, 2, 1.75], 2)))
    print((distribute([1, 2, 3, 4, 5], 4)))
    print(distribute([1, 1.1], 1))
    print(distribute([1, 1.3333334, 1.6, 2], 3))
    print(distribute([0, -0.3333333, 0.667, 1], 3))
