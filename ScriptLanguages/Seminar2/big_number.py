"""
Напишите функцию, которая первым аргументом на вход принимает
строку с цифрами некоторого целого числа. Второй аргумент функции - числа, вхождения кото-
рых нужно найти в переданной строке цифр - является либо целым числом (int), либо кортежем
целых чисел (если их несколько).
Функция должна возвращать количество всех позиций, на которых обнаружены вхождения,
а также отсортированный список обнаруженных позиций. Если передан кортеж, то возвращать
нужно суммарное количество вхождений, а также объединенный отсортированный список пози-
ций найденных чисел. Если длина списка больше чем k, то возвращайте только первые k эле-
ментов, и логируйте факт того, что вхождений на самом деле больше. Параметр k передается
третим аргументом натуральное число, по умолчанию 5.
Замечание. Индексацию цифр ведите с единицы, т.е. первая цифра некоторого числа имеет
индекс один, а не ноль.
Функцию назовите index. Программу сохраните в файле big_number.py.

Пример
assert (1, [1]) == index (’123’, 1)
assert (13 , [1, 1, 2]) == index (’1212122222’, (1, 2, 12), 3)
"""

import logging

logging.basicConfig(format='%(filename)s[function:%(funcName)s]# %(levelname)s %(message)s', level=logging.INFO)


def index(string_num, numbers, k=5):
    """I was thinking about regular expressions, but it's too easy"""

    if type(numbers) is int:
        numbers = (numbers,)
    position_set = {(num, i + 1 + string_num[i:].find(str(num)))
                    for i in range(len(string_num)) for num in numbers if string_num[i:].find(str(num)) != -1}
    positions = [x[1] for x in position_set]
    if k < max(len(positions), k):
        logging.info("Here are some another entries, we simply don't print them")
        return len(position_set), sorted(positions)[: k]
    return len(position_set), sorted(positions)[: len(positions)]


if __name__ == '__main__':
    print(index('1212122222', (1, 2, 12), 13))
    print(index('1524451222', (5, 4, 2,), 10))
    print(index('1524451222', 2, 4))
