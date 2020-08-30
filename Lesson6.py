# f = open('text')
# ints = []
# try:
#     for line in f:
#         ints.append(str(line))
# except ValueError:
#     print('Это не число. Выходим.')
# except Exception:
#     print('Это что еще такое?')
# else:
#     print('Все хорошо.')
# finally:
#     f.close()
#     print('Я закрыл файл')
#     # Именно в таком порядке: try, группа except, затем else, и только потом finally


# print("start")
# try:
#     val = int(input("input number: "))
#     tmp = 10 / val
#     print(tmp)
# except(ValueError, ZeroDivisionError):
#     print("Error")
# print("stop")



# print("start")
# try:
#     val = int(input("input number: "))
#     tmp = 10 / val
#     print(tmp)
# except ValueError as ve:
#     print("ValueError! {0}".format(ve))
# except ZeroDivisionError as zde:
#     print("ZeroDivisionError! {0}".format(zde))
# except Exception as ex:
#     print("Error! {0}".format(ex))
#     print("stop!")




# Вызов исключений в ручную
# try:
#     raise Exception("Some Exeption")
# except Exception as e:
#     print("Exception exeption " + str(e))



# import math
# print(int(math.sqrt(4))) # подключение модуля
#
# from math import sqrt as st
# print(st(4))   # подключение только одной функции
#
# from  math import sqrt, sin, cos
# print(sin(0.2)) # подключение нескольких функций



# def do_something():
#     return "I'm func do_something"
# def more_then_ONE(num):
#     return num > 1
#
# import Piton as my_lib
# print(my_lib.do_something())
# print(my_lib.more_then_one(6))

# import os
# print("os.name = ", os.name)
# print("os.getcwd() = ", os.getcwd())
# dir_path = os.path.join(os.getcwd(), 'NewDir')
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('Такая директория уже существует')
#     os.rmdir(dir_path)
#     print('DELETE')

#
# import sys
# # Список аргументов запуска скрипта,
# # первым аргументом является полный путь к файлу скрипта
# print('sys.argv = ', sys.argv)
# # Список путей для поиска модулей
# print('sys.path = ', sys.path)
# # Полный путь к интерпретатору
# print('sys.executable = ', sys.executable)
# # Словарь имен загруженных модулей
# print('sys.modules = ', sys.modules)
# # информация об операционной системе
# print('sys.platform = ', sys.platform)
# while True:
#     key = input("press 'q' to Exit")
#     if key == 'q':
#         sys.exit()
#         #  Вызов данной функции мгновенно завершает работу модуля (скрипта)

# import sys
# import argparse
#
# def createParser ():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name', nargs='?', default='мир')
#     return parser
# if __name__ == '__main__':
#     parser = createParser()
#     namespace = parser.parse_args(sys.argv[1:])
# print("Привет, {}!".format(namespace.name))

#pypi.com сайт с библиотеками

#sudo apt install python3-pip
#sudo apt install python3-venv
#pip3 install virtualenv
