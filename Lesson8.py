# super().__init__()
# вызов метода от родительского класса

# class Transport:
#     type= "defult"
#     def __init__(self,params = "default"):
#         """
#         какой-то конструктор
#         :param params: возможно, с каким-то параметром
#         """
#         pass
#     def move(self):
#         print("Я транспорт типа: {}. Я умею перемещаться".format(self.type))
#
# class Car(Transport):
#     type = "car"
#     def __init__(self,model,maxSpeed):
#         """
#         Свой конструктор у наследника с доп. параметрами
#
#         """
#         super().__init__()
#         self.model = model
#         self.maxSpeed=maxSpeed
#     def move(self):
#         print("Я транспорт типа: {}. Модель: {}."
#               "Я могу Ехать со скоростью {} км/ч"
#               .format(self.type,self.model,self.maxSpeed))
#
#
#
# transportDefault = Transport()
# car = Car("Tesla model X", 440)
#
# def polimorfism(transport):
#     """
#     Функция демонстрирующая пример полиморфизма.
#     Нам не важно, какой именно транспорт,
#     но мы знаем, что любой транспорт может перемещаться
#     """
#     # hasattr - спрашивает у объекта есть ли заданный атрибут и возвращает либо false либо true.
#     if hasattr(transport,'move'):
#         transport.move()
#     else:
#         print('я не знаю')



# polimorfism(transportDefault)
# polimorfism(car)


# class Vector:
#     def __init__(self, pos):
#         self.x = pos[0]
#         self.y = pos[1]
# # Перегружаем оператор +
#     def __add__(self, other):
#         return Vector((self.x + other.x, self.y + other.y))
#
#     def as_point(self):
#         return self.x, self.y
# # формируем удобное отображение объекта при выводе функции print()
#     def __str__(self):
#         return "V(x:{} y:{})".format(self.x, self.y)
# # Создаем экземпляры класса(объекта)
# v1 = Vector((10,15))
# v2 = Vector((12,10))
# v4 = Vector((36,40))
# # Наши объекты участвуют в операции сложения (+)
# v3 = v1 + v2 + v4
# print(v3)
# # На самом деле это работает так:
# # v3 = v1.__add__(v2)
# # Благодаря перегрузке мы можем использовать более удобную и привычную запись:
# # v3 = v1 + v2

#Расширяем стандартый class dict
# class My_dict(dict):
#     # Добавляем новый метод
#     def new_method(self):
#         return "I'm new_method"
#     # Добавляем дополнительный функционал к существующему методу
#     def __setitem__(self, key, value):
#         print("Setting %r to %r" % (key,value))
#         return super().__setitem__(key,value)
# m_dict = My_dict({1: 2, 2: 3})
# print(m_dict)
# # Данная операция вызывает метод __setitem__
# m_dict["new_key"] = "new_value"
# print(m_dict)
# print(m_dict.keys())
# print(m_dict.new_method())

class Mylist(list):
    def __getitem__(self, offset):
        print('(Indexing % s at % s)' % (self, offset))
        return list.__getitem__(self, offset - 1)
x = Mylist('abc')
print(x)
print(x[1])
print(x[3])
x.append('spam')
print(x)
x.reverse()
print(x)