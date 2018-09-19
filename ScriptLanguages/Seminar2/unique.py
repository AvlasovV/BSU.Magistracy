"""
Напишите функцию, которая принимает на вход последовательность
(кортеж или список) и возвращает список пар из уникальных элементов и количества раз, сколько
они встретились в переданной последовательности. Парой называется кортеж из двух элементов.
Порядок пар в списке не важен.
Замечание. Функцию назовите compress. Программу сохраните в файле unique.py.
"""

import collections


def compress(sequence):
    d = collections.defaultdict(lambda: 0)
    for i in sequence:
        d[i] += 1
    return list(d.items())


print(compress(([1, 12, 3, 4, 1, 3, 12, 4, 1])))
