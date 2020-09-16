# class Student:
#     def __init__(self, name, surname, date, school, class_room):
#         self.name = name
#         self.surname = surname
#         self.date = date
#         self.school = school
#         self.class_room = class_room
#
#     def get_full_name (self):
#                 return self.name + ' ' + self.surname
#     def set_name (self, new_name):
#                 self.name = new_name
#
#
#
# student1 = Student("Alexa", "Spanish", "10.01.1990", "8 licey", "5 A")
# student2 = Student("Nadya", "Gerasimenko", "10.07.1993", "39 gimnacy", "9 A")
# print(student1.class_room)
# print(student2.date)
# print(student1.get_full_name())
# student1.name = 'Petr'
# print(student1.set_name('Petr'))
# print(student2.get_full_name())



class Teacher:
    def __init__(self, name, surname, age, school, class_list):
        self.name = name
        self.surname = surname
        self.date = date
        self.school = school
        self.class_list = class_list

class Person:

    def __init__(self, name, surname, age, school):
        self.name = name
        self.surname = surname
        self.age = age
        self.school = school

    def get_full_name(self):
                return self.name + ' ' + self.surname

    def age_and_number(self):
                return self.age + ' ' + self.school

    def set_name(self, new_name):
                self.name = new_name
persona = Person('Kolya','Kolyanchik','25','licey')
print(persona.age_and_number())

# class Student(Person):
#     def __init__(self, name, surname, date, school, class_room):
#         Person.__init__(self,name,surname,date,school)
#         self._class_room = class_room
#
#     def set_new_class_room(self, class_room):
#         self._class_room = class_room
#
#     def get_class_room(self):
#         return self._class_room
#
class Teacher(Person):
    room = 'de'
    def __init__(self, name, surname, age, school, class_list):
            # Person.__init__(self, name, surname, age, school)
            self._class_list = class_list


    def set_new_class_list(self, class_list):
            self._class_list = class_list

    @property
    def get_class_list(self):
            return self._class_list

# student1 = Student("Alexa", "Spanish", "15", "school", "5 A")
teacher2 = Teacher("Nadya", "Gerasimenko", "40", "schools", "9A,9B,9C")
print(Teacher.room)
print(teacher2.get_class_list)
teacher2.set_new_class_list('21R')
print(teacher2.get_class_list)
# student1.set_name("Kolya")
# print(student1.full_name())
# teacher2.set_new_class_list('5B')
# print(teacher2.get_class_list())


#
# class Student(Person):
#     def __init__(self, name, surname, date, school, class_room):
#         Person.__init__(self,name,surname,date,school)
#         self._class_room = class_room
#
#     def set_new_class_room(self, class_room):
#         self._class_room = class_room
#
#     # @property позволяет обращатся к методу как к атрибуту
    #StaticMethod не принимает аргумент self и тем самым говорит что использование данного метода никак
    # .class_room() --> .class_room
#     @property
#     def get_class_room(self):
#         return self._class_room
#
# student1 = Student("Alexa", "Spanish", "15", "school", "5 A")
# teacher2 = Teacher("Nadya", "Gerasimenko", "40", "schools", "9A,9B,9C")
# print(student1.full_name())
# student1.set_name("Kolya")
# print(student1.full_name())
# print(student1.get_class_room)
# # teacher2.set_new_class_list('5B')
# # print(teacher2.get_class_list())



