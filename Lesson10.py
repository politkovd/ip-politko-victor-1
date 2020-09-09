# class C:
#
#     _x = None
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#             """
#             I'm the 'x' property.
#             """
#             return self._x
#
#     @x.setter
#     def x(self, value):
#             self._x = value
#
#     @x.deleter
#     def x(self):
#                 del self._x
#
# test = C()
#
# print(test.x)
# test.x = 12
# print(test.x)
# del test.x
# print(test.x)



# import random
#
#
# class MusicGenre:
#
#     '''  Базовый класс жанра для музыкальной библиотеки.
#          Определяет название жанра и его рейтинг в библиотеке.
#     '''
#
#     genre_count = 0
#
#     def __init__(self, name, rating):
#         self._name = name
#         self._rating = rating
#         MusicGenre.genre_count += 1
#
#     def __del__(self):
#         MusicGenre.genre_count -= 1
#
#     def rate_up(self, point):
#         self._rating += point
#
#     def rate_down(self, point):
#         self._rating -= point
#
#     def rating(self):
#         return self._rating
#
#
# class DrumAndBase(MusicGenre):
#     def rating(self):
#         # "Случайная" накрутка рейтинга
#         if random.randint(0, 4) == 1:
#             return self._rating + 1
#         else:
#             return self._rating
#
#
# group = DrumAndBase ("Pendulum", 65.7)
# group.rate_up(5.5)
# print("Рейтинг исполнителя {}: {}".format(group._name, group.rating()))
#
# class PromoConcert:
#     ''' Промо-концерт - улучшает рейтинг исполнителя
#     '''
#     points = 5.00
#     def go_up(self):
#         self.rate_up(self.points)



# class Gossip:
#
#     '''
#        Сплетни, слухи - снижают рейтинг
#     '''
#
#     points = 2.70
#     def go_down(self):
#         self.rate_down(self.points)
#
# #  Класс, использующий механизм множественного наследования
# class SuperDrums (DrumAndBase, PromoConcert, Gossip):
#     def rate_up(self, points):
#         super().rate_up(points)
#
#     def rate_down(self, points):
#         super().rate_down(points)
#
# artist = SuperDrums("RonWllsJS", 90.00)
# print(artist.rating())
# artist.go_up()
# print(artist.rating())
# artist.go_down()
# print(artist.rating())



# class A:
#     def genre(self):
#         return ['Blues']
#
#     def artist(self):
#         return []
#
#
# class B(A):
#     def genre(self):
#         return ['Electric blues'] + super().genre()
#
#
# class C(A):
#     def artist(self):
#         return ['B.B. King'] + super().artist()
#
#
# class D(A): pass
#
#
# class E(B):
#     def genre(self):
#         return ['Soul blues'] + super().genre()
#
#
# class F(B):
#     def genre(self):
#         return ['Blues rock'] + super().genre()
#
#     def artist(self):
#         return ['Eric Clapton'] + super().artist()
#
# class G(C, D): pass
#
#
# class H(E, F, G):
#     def genre(self):
#         return ['Boogie rock'] + super().genre()
#
#
# if __name__ == "__main__":
#     H = H()
#     print('List of artists: ')
#     for artists in H.artist():
#         print(' - ' + artists)
#
#     print ('List of linked genres: ')
#     for genre in H.genre():
#         print(' - ' + genre)
#


# from  abc import ABCMeta, abstractmethod, abstractproperty
#
# class Foo(metaclass=ABCMeta):
#     @abstractmethod
#     def spam(self, a, b):
#         pass
#     @abstractproperty
#     def name(self):
#         pass
#
# class Grok:
#     def spam(self, a, b):
#         print("Grok.spam")
#
# Foo.register(Grok) # Зарегестрирует Grok, как наследующий абстрактный базовый класс Foo

#
# class Account(object):
#     __slots__ = ('name', 'balance')
#
# acc = Account()
# # acc.x = 13 # Ошибка
#
# acc.name = '1'
# acc.balance = '122'
# print(acc.name)
# print(acc.balance)

# class TypedProperty:
#     def __init__(self, name, type_name, default=None):
#         self.name = "_" + name
#         self.type = type_name
#         self.default = default if default else type_name()
#
#     def __get__(self, instance, cls):
#         return getattr(instance, self.name, self.default)
#
#     def __setitem__(self, instance, value):
#         if not isinstance(value, self.type):
#             raise TypeError("Значение должно быть типа %s" % self.type)
#         setattr(instance,self.name, value)
#
#     def __delete__(self, instance):
#         raise AttributeError("Невозможно удалить атрибут")
#
#
# class Foo:
#     name = TypedProperty("name", str)
#     num = TypedProperty("num", int, 42)
#
#
# f = Foo()
# a = f.name          # Неявно вызовет Foo.name.__get__(f, Foo)
# print(a)
# print(f.name)
# # f.name = "Гвидо" # Вызовет Foo.__set__(f, "Гвидо")
# a = 1
# print(a)
# del f.name          # Вызовет Foo.name.__delete__(f)




class DocMeta(type):
    def __init__(self, clsname, bases, clsdict):
        for key, value in clsdict.items():
            if key.startwith(value, "__call__"):continue

            if not getattr(value, "__doc__"):
                raise TypeError("%s must have a docstring" % key)

        type.__init__(self, clsname, bases, clsdict)


class Documented(metaclass=DocMeta):
    pass

class Foo(Documented):
    def spam(self, a, b):
        '''
          Метод spam делает кое-что
        '''
        pass
    def boo(self):
        print('A little problem')