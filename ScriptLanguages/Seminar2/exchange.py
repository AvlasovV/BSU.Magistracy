"""
Напишите функцию, подсчитывающую количество различных способов
выдать со счета сумму от 0 до 50 копеек монетами по 1, 2, 5 и 10 копеек.
Замечание. Программу сохраните в файле exchange.py, функцию назовите  exchange_money.
"""

COINS = (1, 2, 5, 10)


def get_count(money, index):
    if money < 0 or index < 0: return 0
    if money == 0 or index == 0: return 1
    return get_count(money, index - 1) + get_count(money - COINS[index], index)


def exchange_money(money):
    if money == 0: return 0
    return get_count(money, len(COINS) - 1)

