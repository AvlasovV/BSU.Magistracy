"""
Напишите функцию, возвращающую число, битовое представление
которого является 𝑘-тым членом последовательности Морса–Туэ (последовательность OEIS номер
A010060, https://en.wikipedia.org/wiki/Thue-Morse_sequence). Значение 𝑘 полагайте допустимым
целым числом, большим либо равным нуля.
Подсказка. Возможно, полезной будет эта ссылка: https://stackoverflow.com/a/12790495.
Замечание. Программу сохраните в файле thue_morse.py, функцию назовите get_sequence_item.
О быстрой скорости роста числа не беспокойтесь. Постарайтесь в решении обойтись без использования
строк и списков и использовать операции с числами.
"""


def get_inversion(num):
    deegre = num.bit_length()
    inversion = 2 ** (deegre + 1) - 1 - num
    # print({num : bin(num), inversion : bin(inversion)})
    return inversion


def get_sequence_item(k):
    # st = 0
    number = 0
    if k == 0:
        return 0
    for i in range(1, k + 1):
        tail = get_inversion(number)
        res = (number << (2 ** (i-1))) + tail
        # print({'k-term' : i, number : bin(number), tail : bin(tail), 'Result' : bin(res)})  # we can see number, inversed tail and result
        number = res
    return number
