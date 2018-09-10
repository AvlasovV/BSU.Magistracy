"""Напишите программу, которая будет выводить через пробел все нечет-
ные числа от 1 до 101 (включительно), попутно заменяя числа, которые делятся на 3, на Fizz,
делящиеся на 7 – на Buzz, а делящиеся и на 3, и на 7 – на FizzBuzz. """

""" While оказался быстрее for на дистанции до 100000, затем вперёд вырывается for,
 но т.к. нам нужен маленький промежуток, то оставил while-вариант"""

import time

max_value = 102


def cycle_for():
    for i in range(1, max_value, 2):
        if i % 3 == 0:
            if i % 7 == 0:
                print('FizzBuzz', end=" ")
            print('Fizz', end=" ")
            continue
        elif i % 7 == 0:
            print('Buzz', end=" ")
            continue
        else:
            print(i, end=" ")


def cycle_while():
    i = 1
    while i < max_value:
        if i % 3 == 0:
            if i % 7 == 0:
                print('FizzBuzz', end=" ")
            print('Fizz', end=" ")
            i += 2
            continue
        elif i % 7 == 0:
            print('Buzz', end=" ")
            i += 2
            continue
        else:
            print(i, end=" ")
            i += 2


start_while = time.perf_counter()
cycle_while()
start_while = time.perf_counter() - start_while

# start_for = time.perf_counter()
# cycle_for()
# start_for = time.perf_counter() - start_for

# f = open("output", 'w')
# f.write('\nFor-cycle: ' + str(start_for))
# f.write('\nWhile-cycle: ' + str(start_while))
