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


def index(string_num, numbers, k = 5):
    # numbers = tuple(numbers)
    # position_list = [(num, i + 1 + string_num[i:].find(str(num)))
    #                  for i in range(len(string_num)) for num in numbers if string_num[i:].find(str(num)) != -1]
    position_set = {(num, i + 1 + string_num[i:].find(str(num)))
                     for i in range(len(string_num)) for num in numbers if string_num[i:].find(str(num)) != -1}
    positions = [x[1] for x in position_set]
    positions.sort
    i = 0
    while i < len(position_set) or i < k:
        positions

    # position_list
    # position_list = sorted(set(position_list))
    # return len(position_list), set(position_list)
    return len(position_set), sorted(positions)


print(index('1212122222', (1, 2, 12)))
print(index('1212122222', (2,)))
# print