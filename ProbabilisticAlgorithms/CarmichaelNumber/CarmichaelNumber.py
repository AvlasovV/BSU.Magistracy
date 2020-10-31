"""
Задача 3.2. Число Кармайкла
Имя входного файла: carmichael.in
Имя выходного файла: carmichael.out
Положительное целое число называется составным, если имеет больше двух натуральных делителей.
Составное число n называется числом Кармайкла, если для любого x от 1 до n - 1, взаимно простого с n, верно, что
x^{n - 1} ≡ 1(modn). Необходимо проверить, является ли заданное число числом Кармайкла.
Формат входных данных
В первой строке записано число t наборов входных данных (1≤t≤3000).
Каждая из последующих t строк содержит натуральное число 0 ≤ n_i ≤ 10 ^ 15

Формат выходных данных
Для каждого числа на входе выведите в отдельной строке Yes, если число является числом Кармайкла, либо No в противном случае.
Пример
carmichael.in
3
560
561
562
carmichael.out
No
Yes
No
"""

import random
import math

random.seed()


def gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    return a


def get_random_coprime_number(number):
    """Fermat primality test"""
    while True:
        coprime = random.randint(2, number - 1)
        if gcd(coprime, number) == 1:
            return coprime


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

    k = 15  # For Miller-Rabin test
    m = 20  # For Fermat test
    with open("carmichael.in", "r") as input, open("carmichael.out", "w") as output:
        count = int(next(input))
        for i in range(count):
            number = int(next(input))
            if number == 0 or number == 1:
                output.write("No\n")
                continue
            if is_prime(number, k):
                output.write("No\n")
                continue
            else:
                for i in range(m):
                    if pow(get_random_coprime_number(number), number - 1, number) != 1:
                        output.write("No\n")
                        break
                else:
                    output.write("Yes\n")

    # for i in range(10 ** 8):
    #     number = i
    #     if number == 0 or number == 1:
    #         continue
    #     if is_prime(number, k):
    #         continue
    #     else:
    #         for i in range(m):
    #             if pow(get_random_coprime_number(number), number-1, number) != 1:
    #                 # output.write("No\n")
    #                 break
    #         else:
    #             #output.write("Yes\n")
    #             print("Carmichael number = ", number)
