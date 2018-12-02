"""Задание 4. (2.5 балла). Реализуйте контекстный менеджер handle_error_context и декоратор
handle_error, которые позволяют обрабатывать и логировать ошибки в зависимости от
переданных параметров:
∙ re_raise – флаг, отвечающий за то, будет произведен проброс исключения (типы исключений
для обработки заданы параметром exc_type – см. ниже) из блока/функции на уровень
выше или нет (по умолчанию True);
∙ log_traceback – флаг, отвечающий за то, будет ли при возникновении исключения типа
exc_type отображен traceback (по умолчанию True);
∙ exc_type – параметр, принимающий либо отдельный тип, либо непустой кортеж типов исключений,
которые должны быть обработаны (для всех остальных блока except не будет)
– значение по умолчанию выставьте тип Exception;
∙ tries – параметр, означающий количество попыток вызова функции, прежде чем бросить
исключение (по умолчанию 1, значение None – бесконечные попытки, неположительные
значения недопустимы);
∙ delay – значение задержки между попытками в секундах (может быть float, по умолчанию
0);
∙ backoff – значение множителя, на который умножается delay с каждой попыткой (по умолчанию
1, см. пример)

Для обработки и логирования traceback можно использовать функцию sys.exc_info() и схожие
ей, модуль traceback, а логирование осуществлять с помощью глобального для модуля объекта
logger – Logger’а из стандартной библиотеки (модуль logging).
Обратите внимание, что при реализации декоратора и менеджера контекста код должен быть
переиспользован – простого копирования требуется избежать. Реализовывать менеджер контекста
с помощью класса также не нужно.
Сохраните все в файле error_handling.py.

Замечание. Применение аналога SafeRequest в связке с retry – хорошая практика при
выполнении запросов.

Замечание (01.12.2018): параметры tries, delay и backoff нужно реализовать только в декораторе handle_error.
В менеджере контекста handle_error_context эти три параметра не применимы.

Пример 1
# log traceback , re - raise exception
with handle_error_context ( log_traceback =True , exc_type = ValueError ):
raise ValueError ()
Пример 2
# suppress exception , log traceback
@handle_error ( re_raise = False )
def some_function ():
x = 1 / 0 # ZeroDivisionError
some_function ()
print ( 1 ) # line will be executed as exception is suppressed


Пример 3
# re - raise exception and doesn ’t log traceback as exc_type doesn ’t match
@handle_error ( re_raise =False , exc_type = KeyError )
def some_function ():
x = 1 / 0 # ZeroDivisionError
some_function ()
print ( 1 ) # line won ’t be executed as exception is re - raised

Пример 4
Пусть в примере ниже random.random() последовательно возращает 0.2, 0.5, 0.3, тогда декоратор
должен вызвать функцию some_function, перехватить исключение, подождать 0.5 секунды,
попробовать еще раз, подождать 1 секунду, попробовать еще раз и пробросить исключение.
import random
@handle_error ( re_raise =True , tries =3 , delay =0 .5 , backoff =2 )
def some_function ():
if random . random () < 0 . 75:
x = 1 / 0 # ZeroDivisionError
some_function ()
"""

from contextlib import contextmanager
from time import sleep
import logging


@contextmanager
def handle_error_context(re_raise=True, log_traceback=True, exc_type=Exception):
    try:
        yield
    except exc_type as err:
        if log_traceback:
            logging.exception(str(err))
        if re_raise:
            raise err
    # print("123LyaLya")


def handle_error(re_raise=True, log_traceback=True, exc_type=Exception, tries=1, delay=0, backoff=1):

    def handle_error_decorator(function):
        def wrapper(*args, **kwargs):
            nonlocal tries, delay, backoff
            while True:
                try:
                    with handle_error_context(True, log_traceback, exc_type):
                        res = function(*args, **kwargs)
                except exc_type as err:
                    if tries is not None and tries > 0:
                        tries -= 1
                    elif tries is None:
                        pass
                    elif tries == 0:
                        if re_raise:
                            raise err
                        else:
                            return
                else:
                    return res
                if delay > 0:
                    sleep(delay)
                    delay *= backoff
        return wrapper

    return handle_error_decorator


if __name__ == "__main__":

    # with handle_error_context(re_raise=False, log_traceback=True, exc_type=ValueError):
    #     raise ValueError()
    # print(234)


    it = iter([0.2, 0.5, 0.3])
    @handle_error(re_raise=True, tries=3, delay=0.5, backoff=2)
    def some_function():
        if next(it) < 0.75:
            x = 1 / 0  # ZeroDivisionError


    res = some_function()
