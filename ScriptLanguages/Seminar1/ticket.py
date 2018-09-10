"""Билетик называется счастливым, если сумма первых трех цифр его
номера равна сумме последних цифр. Напишите функцию, принимающую номер билета и воз-
вращающую номер ближайшего счастливого билета (если их два – то любой из них). Номер
переданного билета полагайте допустимым целым шестизначным числом (без нулей в начале).
Замечание. Программу сохраните в файле ticket.py, функцию назовите get_nearest_lucky_ticket.
"""


def get_nearest_lucky_ticket(ticket_number):
    return searching_lucky_tickets(ticket_number)[0]


def find_sum(ticket_number, mode='first'):
    sum = 0
    if mode == 'first':  # return sum of 3 first digits
        for i in str(ticket_number // 1000):
            sum += int(i)
    elif mode == 'last':  # return sum of 3 last digits
        for i in str(ticket_number % 1000):
            sum += int(i)
    elif mode == 's':  # return sum of all digits
        for i in str(ticket_number):
            sum += int(i)
    else:
        print("Wrong mode!")
    return sum


def find_num(ticket_number, mode='first'):
    if mode == 'first':
        return ticket_number // 1000
    elif mode == 'last':
        return ticket_number % 1000
    else:
        print("Wrong mode!")


def searching_lucky_tickets(ticket_number):
    first_num = find_num(ticket_number, 'first')
    last_num = find_num(ticket_number, 'last')
    first_sum = find_sum(ticket_number, 'first')
    last_sum = find_sum(ticket_number, 'last')

    if last_sum == first_sum:
        return ticket_number, 0

    min_difference = 1000
    best_lucky_ticket = None

    for i in (first_num - 1, first_num,  first_num + 1):
        result_set = decomposition_of_number(find_sum(i, 's'))
        for j in result_set:
            lucky_ticket = i * 1000 + (j[0] * 100 + j[1] * 10 + j[2] * 1)
            difference = abs(ticket_number - lucky_ticket)
            if difference < min_difference:
                min_difference = difference
                best_lucky_ticket = lucky_ticket

    return best_lucky_ticket, min_difference



def decomposition_of_number(number):  # decompose into 3 terms, I think it should be recursion but now it's not :)
    result_set = set()
    for i in range(0, 10):
        if i > number: break
        for j in range(0, 10):
            if j + i > number: break
            for k in range(0, 10):
                if k + i + j > number:
                    break
                elif k + i + j == number:
                    result_set.add(tuple([i, k, j]))
    return result_set


# testing part
# print(decomposition_of_number(2))
# print(set([1,3,5]) == set([5,5,3,3,1]))
# print(searching_lucky_tickets(100100))
# print(get_nearest_lucky_ticket(100000))
