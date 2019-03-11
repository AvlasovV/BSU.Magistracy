"""
Задача 3.1. Проверка на простоту
Имя входного файла: primality.in
Имя выходного файла: primality.out
Ограничение по времени: 2 с
Ограничение по памяти: 1024 МБ
Натуральное число называется простым, если оно имеет ровно два натуральных делителя.
Необходимо проверить, является ли заданное число простым.

Формат входных данных
В первой строке записано число t наборов входных данных (1 ≤ t ≤ 3 000).
Каждая из последующих t строк содержит натуральное число pi (0 ≤ pi ≤ 10^15).
Формат выходных данных
Для каждого числа на входе выведите в отдельной строке Yes, если число является простым, либо No в противном случае.
Пример
primality.in
3
5
8
13
primality.out
Yes
No
Yes
Замечание
При решении задачи не допускается использование метода BigInteger.isProbablePrime и его аналогов.
"""
import random
import math
random.seed()


def fast_pow(number):
    pass


def is_prime(number, iterations=40):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number == 1:
        return False

    t = number - 1
    s = 0
    # while True:
    #     if t % 2 == 0:
    #         s += 1
    #         t = t / 2
    #     else:
    #         break
    s = int(math.log(t & -t, 2))
    t = t / (2 ** s)

    # main cycle
    for _ in range(iterations):
        a = random.randint(3, number - 1)
        x = pow(a, int(t), number)
        if x == 1 or x == number - 1:
            continue
        for i in range(s - 1):
            x = pow(x, 2, number)
            if x == 1:
                return False
            elif x == number - 1:
                break
        else:
            return False
    return True


if __name__ == "__main__":
    # import cProfile, pstats, io
    # from pstats import SortKey
    # """Here profiling code starts"""
    # pr = cProfile.Profile()
    # pr.enable()

    k = 20
    with open("primality.in", "r") as input, open("primality.out", "w") as output:
        count = int(next(input))
        for i in range(count):
            number = int(next(input))
            if is_prime(number, k):
                output.write("Yes\n")
            else:
                output.write("No\n")

    """ending profiling"""
    # pr.disable()
    # s = io.StringIO()
    # sortby = SortKey.CUMULATIVE
    # statistics = pstats.Stats(pr, stream=s).sort_stats(sortby)
    # statistics.print_stats()
    # print(s.getvalue())