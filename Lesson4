# for i in range(0,8,2): # range(1,2,3): 1 - начало, 2 - конец, 3 - шаг

# print(abs(-2))

# print(max([1,2,3,4,5]))  #min/max


# x = round(sum([2.56,1,12,15]),2)
# print(x)

# x = type({'n'})
# print(x)


# x = [1,2,3,4]
# for i,y in enumerate(x): # возвращает пару индекс и значение
#     print(i,y)

# def summ(a,b):
"""
      :param a:
      :param b:        comment
      :return: a + b

"""
#     return a + b
#
# a = 5
# b = 6
# z = summ(a,b)
# print(z)

#
# f = lambda x: x ** 2
# print(f(4))
#
# print((lambda x: x ** 2)(4))


x = 5  #глобальная переменная - доступна в любом месте данного модуля(файла)

def outside():
    y = 10   #доступна в теле данной функции + во всех вложенных
    def inside():
        z = 15 #  доступная только в теле данной функции
        print('inside x: {}, y: {}, z: {}'.format(x,y,z))
    inside()
    print('outside x: {},y: {}, z: {}'.format(x,y,'z недоступна'))
outside()
print('inside x: {}, y: {}, z: {}'.format(x, 'y недоступна', 'z недоступна'))
x = 5
def wrapper():
    def test1():
        x = 10
        print('test1 x =',x)
    def test2():
        print('test2 x =',x)
    def test3():
        global x
        print('test3 x=',x)
        x = 25
    test1()
    test2()
    test3()
wrapper()
print('after wrapper x = ', x)


# def average (*args):
#     summ = 0
#     for arg in args:
#         summ = summ + arg
#     return summ/len(args)
# print(average(1,2,3))

# def print_info(**kwargs):
#     print("You name is %s %s. You age is %s. And your address is: %s"%
#           (kwargs["name"],kwargs["surname"],kwargs["age"],kwargs["adress"]))
#     print_info(name="Василий",surname="Иванов",age="12",adress= "ул.Белана 22")
#
#     def print_info(name,surname,age,adress):
#         print(f"You name is", {name}, {surname} ,{age} ,{adress})
#         print_info(name="Василий", surname="Иванов", age="12", adress="ул.Белана 22")


# def welcome(name= "Инкогнито"):
#  print(f"Hello {name}")
# welcome('User')
# welcome()

#
# a = [1,2]
# b = [3,4]
# print(zip(a,b))


# a = [1,2,9]
# b = [3,4,5]
# c = [6,7,4,8]
#
# for i in zip(a,b,c):
#
#  print (i)
#
 #zip - итериратор который генерирует серию множеств, содержащий элементы из каждой итерации.



# print(list(map(lambda x: x*x, [2,5,12,-2])))
#
# print(list(map(len , ['2','5','12','-2'])))
#
# #map() позволяет применить функцию к каждому элементу последовательности,
# # результаты возвращает в виде итератора
#
# # filter()
# print(list(filter(lambda x: x >= 3,[1, 7,13.8, 0.002, 5, 3])))
# print(list(filter(len,['','not null','lol','','10'])))
# # отбрасывает те элементы, для которых функция возвращает False.

# import  os
# path = os.path.join('text')
# # f = open(path,'r',encoding= 'UTF -8')
# # wanted_symbol = '+'
# # for line in f:
# #      if wanted_symbol in line:
# #         print(line)
# #         break
# # print(f.readlines())
# # f.close()
#
#
# with open(path, 'r', encoding='UTF-8') as f:
#     print(f.readlines())
#     f.close()
# my_file = open('text', 'w')
# my_file.write("Python nice")
# my_file.close()

# Запись текста в фАЙЛ
