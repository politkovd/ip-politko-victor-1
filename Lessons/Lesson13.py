# def foo():
#     x = 13
#     a = 10
#     array = ['Lol', 'Kek']
#
#     def helloman():
#         print("Привет, Мистер{}".format(x))
#         print("Вот твой список клиентов: {}".format(array))
#     return helloman
#
# bar = foo()
# bar()
# # Посмотрим какие есть атрибуты у helloman
# print(dir(bar))
#
# # Если посмотрим, то увидим, что в замыкании есть два объекта
# print(bar.__closure__)
# # Выведим их
# for attr in bar.__closure__:
#     print(attr.cell_contents)
#
# # Зададим ссылку. array2 ссылается на тот же объект в памяти?
# array2 = bar.__closure__[0].cell_contents
#
# # Проверим. Добавим еще один элемент в массив и выполним функцию еще раз.
# array2.append('Cheburek')
# bar()


# from urllib.request import urlopen
#
#
# def page(url):
#     def get():
#         return urlopen(url).read()
#
#     return get
#
#
# python = page("http://www.python.org")
# jython = page("http://www.jython.org")
#
# pydata = python()
# jydata = jython()
# print(pydata[:100])
# print(jydata[:100])
# print(python.__closure__)
# print(python.__closure__[0].cell_contents)


# def countdown(n):
#    e = 0
#    def next():
#        nonlocal n, e
#        e += 1
#        r = n
#        n -= 1
#        return r
#    return next
#
# # Пример использования
# next = countdown(10)
# print(next.__closure__[0].cell_contents)
# print(next.__closure__[1].cell_contents)
# print("\n")
# while True:
#    v = next() # Получить следующее значение
#    print(v)
#    if not v: break


# @trace
# def square(x):
#    return x * x  #= def square(x):
#                     # return x * x
#
#                 # square = trace(square)


# def some_decorator(func):
#    def dop_func():
#        print("Do something before")
#        func()
#        print("Do something after")
#    return dop_func
#
#
# def some_decorator2(func):
#    def dop_func(*args):
#        print("Do something")
#        return func(*args)
#    return dop_func
#
# @some_decorator
# def show_some():
#    print("Hello!")
#
#
# @some_decorator2
# def pow(x, val):
#    return x ** val
#
# show_some()
# print(pow(2, 4))
# print(pow(3, 3))


# Декоратор в виде класса
#
# class Log():
#     def __init__(self):
#         pass
#
#     # Магический метод __call__ позволяет обращаться к
#     # объекту класса, как к функции
#     def __call__(self, func):
#         def decorated(*args, **kwargs):
#             res = func(*args, **kwargs)
#             print(f'log: {func.__name__}({args}, {kwargs}) = {res}')
#             return res
#
#         return decorated
#
#
# @Log()
# def square(x, y, c, d):
#     return round((((x * x) + y) / c) ** d, 2)
#
#
# square(4, 5, 6, 10)


# def makebold(fn):
#    def wrapped():
#        return "<b>" + fn() + "</b>"
#    return wrapped
#
# def makeitalic(fn):
#    def wrapped():
#        return "<i>" + fn() + "</i>"
#    return wrapped
#
# @makebold
# @makeitalic
# def hello_with_dec():
#    return "Hello decorators!"
#
# def hello_simple():
#    return "Hello decorators!"
#
# print(hello_with_dec())
#
# # Добьемся аналогичного результата
# hello_simple = makebold(makeitalic(hello_simple))
# print(hello_simple())


# def factorial(n):
#     """ Вычисляет факториал числа. Например:
#        >>> factorial(6)
#        720
#        privet
#    """
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial.__doc__)


# from functools import wraps
#
# def bad_decorator(func):
#    @wraps(func)
#    def call(n):
#        return func(n)
#    call.__doc__ = "Doc-a теперь под моей юрисдикцией!"
#    call.easter = "Оп-па! Пасхалочка."
#    return call
#
# @bad_decorator
# def factorial(n):
#    """ Вычисляет факториал числа. Например:
#        >>> factorial(6)
#        720
#    """
#    if n <= 1:
#        return 1
#    else:
#        return  n * factorial(n-1)
#
# print(factorial.__doc__)
# print(factorial.__name__)
# print(factorial.easter)


# # Трехэтажный декоратор
# from functools import wraps
#
#
# def repeat(n=5):
#     def _repeat(f):
#         @wraps(f)
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 f(*args, **kwargs)
#
#         return inner
#
#     # не забываем ее вернуть!
#     return _repeat
#
#
# @repeat(3)
# def foo(test):
#     print(f'hello {test}')
# foo('test')
#


# Логирование
import logging
logging.basicConfig(
   filename = "app.log",
   format = "%(levelname)-10s %(asctime)s %(message)s",
   level = logging.INFO
)
log = logging.getLogger("app")
# Записать сообщение, используя позиционные аргументы форматирования
host = 'localhost'
port = 7777
log.critical("Can't connect to %s at port %d", host, port)
# Записать сообщение, используя словарь значений
parms = { 'host' : 'www.python.org',
'port' : 80
}
log.critical("Can't connect to %(host)s at port %(port)d", parms)