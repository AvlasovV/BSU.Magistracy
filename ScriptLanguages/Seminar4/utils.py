"""Задание 1. (0.5 балла). Реализуйте декоратор profile, который при вызове функции подсчитывает
время выполнения этой функции, выводит его на экран и возвращает результат вызова
функции.
Рассмотрите стандартный модуль timeit и, в частности, функцию default_timer для измерения
времени выполнения.
Декоратор сохраните в файле utils.py.

Пример
@profile
def some_function ():
return sum( range ( 1000 ) )
result = some_function () # return a value and print execution time

Задание 2. (0.5 балла). Реализуйте менеджер контекста timer, который посчитает время
выполнения блока и выведет его на экран.
Сохраните менеджер контекста в файле utils.py.
Пример
with timer ():
print ( sum ( range ( 1000 ) ) )
# print execution time when calculation is over

Задание 3. (1.5 балла). Реализуйте callable-класс SafeRequest, которой позволяет выполнить
запрос к ресурсу, ограничив его по timeout, а также вернуть некоторое значение по умолчанию
в случае получения кода ответа 404, если оно установлено. Если же значение по умолчанию не
установлено, то при таком коде ответа возникшее исключение должно быть проброшено дальше.
В конструкторе класса передавайте два параметра:
∙ timeout – время таймаута в секундах, может быть float, по умолчанию 3;
∙ default – None или not set (см. паттерн в лекциях) – значение по умолчанию, если страница
отсутствует.
Предполагайте, что запрос выполняется с помощью библиотеки requests. Для проверки значения
timeout можно использовать аннотации типов (PEP-484).
Cохраните класс в файле utils.py.

Пример
import requests
# ordinary way; requests . get may be used
data = requests . request (’get ’, ’http :// yandex .ru/’, headers ={...})
# timeout added to request , default value might be used
safe_request = SafeRequest ( timeout =5 , default = None )
data = safe_request (’get ’, ’http :// yandex .ru/’, headers ={ ...})
"""

from timeit import default_timer
import requests


def profile(func):
    """Actually, decorators work not too good with recursive functions so be careful.
    If you want to exec recursive function, don't use @<decor_name> statement, just use <decor_name(your_function)> in
    your code.
    Good answer about it is here:
    https://stackoverflow.com/questions/10757871/decorating-recursive-functions-in-python
    """

    def wrapped(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print("Running {} took {} seconds.".format(func.__name__, default_timer() - start))
        return result

    return wrapped


class timer:
    def __init__(self):
        self.start = default_timer()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("This block of code get {} seconds.".format(default_timer() - self.start))
        if exc_type:
            print("WE HAVE AN ERROR BUT WE SKIP IT. Error: {}, {}".format(exc_type.__name__, exc_val))
            return True


class SafeRequest:
    def __init__(self, timeout=3, default=None):
        assert isinstance(timeout, (int, float)), "Wrong timeout type"
        self.timeout = timeout
        self.default = default

    def __call__(self, *args, **kwargs):
        r = requests.request(*args, **kwargs, timeout=self.timeout)
        if r.status_code == 404 and self.default is not None:
            # print(self.default)
            return self.default
        elif r.status_code == 404 and self.default is None:
            r.raise_for_status()
        else:
            return r


# There are some test functions and one another decorator for memoization
def cache_decor_for_recursive_function(func):
    """I have read about cache for recursive functions so let's try
    Just good article with the same code:
    https://www.andreagrandi.it/2015/08/31/understanding-python-decorators-optimizing-a-recursive-fibonacci-implementation/
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


def factorial(n):
    return factorial(n - 1) * n if n > 1 else 1


@cache_decor_for_recursive_function
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 2 else n


if __name__ == "__main__":
    # print()
    # print(factorial(100))
    decor_factorial = profile(factorial)  # Good variant or running recursive functions
    print(decor_factorial(100))

    # print(profile(fibonacci)(40))
    # print(profile(fibonacci)(40))
    print(profile(fibonacci)(400))  # Wonderful result for Fibonacci!
    with timer() as t:
        decor_factorial = profile(factorial)
        print(decor_factorial(500))
        print(profile(fibonacci)(500))
        raise Exception
    print("Abra Kada BRyaaaaau")

    safe_request = SafeRequest(timeout=2, default="PamPam")
    data = safe_request(r'get', r'http://yandex.ru/1231')
    print(data)

    safe_request = SafeRequest()
    data = safe_request(r'get', r'http://yandex.ru/1231')
    print(data)