"""
Напишите функцию, которая принимает один аргумент n – натуральное
число – и возвращает все простые числа, не превосходящие n. Используйте comprehensions для
решения задачи.
Полный балл за задачу будет выставлен только в случае написания функции из одного
comprehension выражения.
Функцию назовите get_primes. Программу сохраните в файле primes.py.
"""

from math import sqrt


def get_primes(n):
    return [x for x in range(2, n + 1) if all([False for k in range(2, int(sqrt(x)) + 1) if x % k == 0])]


def check_prime(k):
    return all([False for x in range(2, int(sqrt(k)) + 1) if k % x == 0])


if __name__ == '__main__':
    for i in range(0, 20):
        print('Number ' + str(i), get_primes(i))
        check_prime(i)
    result_set = set()
    for i in range(2, 100):
        result_set.add(get_primes(i)[-1])
    print(result_set)
