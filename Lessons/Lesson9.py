# with open('path/to/some/sdfgsdgsdgsdg') as file_1,\
#      open('asdfasfasfasf', 'w') as file_2:
#         file_2.write(file_1.read())
#         print(file_2)

        # import os  стандартные библиотеки
        # import  сторонняя библиотека
        # import builder  ваши модули

        # Правильно
        # spam(ham[1], {eggs: 2})
        # Неправильно
        # spam( ham[ 1 ], { eggs:2})


# {
#         "firstName": "Иван",
#         "lastName": "Иванов",
#         "address": {
#                 "streetAddress": "Московское шоссе, 101, кв.101",
#                 "city": "Ленинград",
#                 "postalCOde": "101101"
#         },
#         "phoneNumbers": [
#                 "812 123-1234",
#                 "916 123-4567"
#         ]
# }
# import json
# data = {'name': 'Vasya',
#         'surname': 'Petrov',
#         'address': {'city': 'Hollywood', 'Street': 'NEW'}
#         }
# with open('l9_file.json', 'w') as outfile:
#         json.dump(data,outfile) #json.dump - запись
# with open('l9_file.json', 'r') as f:
#         data2 = json.loads(f.read()) #json.loads - считывание json и приведение его к python
#         print(data2)


class WorkerBuilder:
        def __init__(self, d):
                for key, value in d.items():
                        setattr(self, key, value)
worker = WorkerBuilder({"name": "Petr","surname": "Ivanov","age": 30})
worker2 = WorkerBuilder({"name": "Denis","surname": "Kovtun","age": 40})
print(worker.name)
print(worker.surname)
print(worker2.age)

class HousingBuilder:
        def __init__(self, d):
                for key, value in d.items():
                        setattr(self,key,value)
home = HousingBuilder({"type": "Квартира","square": "220","rooms": 4})

home2 = HousingBuilder({"type": "Квартира","district": "45","rooms": 4})

print(home.rooms)
print(home2.district)

# для паттерна builder библиотека abc
# coding:utf - 8
# python 3


class A:
        def f(self):
                print('A: вызываем метод f')

        def g(self):
                print('A: вызываем метод g')


class C:
        def __init__(self):
                self.A = A()

        def f(self):
                return self.A.f()

        def g(self):
                return self.A.g()


c = C()

c.f() #А: вызываем метод f

c.g() #A: вызываем метод g

