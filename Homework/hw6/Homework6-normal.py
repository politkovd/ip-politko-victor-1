# Задача:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
from easy import creating_dirs, deleting_dirs, main_contents

path = '/Users/viktorpolitko/VSCODE/ip-politko-victor-1'
os.getcwd()
print(os.getcwd())


def main_menu():
    while True:
        print("""   
                    Меню 
    Выберите цифру для необходимого действия:
            Перейти в нужную папку - 1                    
        Просмотреть содержимое текущей папки - 2
                Удалить папку - 3               
                Создать папку - 4
                Выход из программы - 5
                """)

        button = input()
        try:
            if button == '1':
                dir_name = input('Название папки для перехода: ')
                if dir_name in main_contents():
                    os.chdir(dir_name)
                    print('Успешно выполнен переход в папку %s' % dir_name)
                    print(os.getcwd())
                else:
                    print('Невозможно перейти в папку %s. Папки не существует' % dir_name)
            elif button == '2':
                for i in main_contents():
                    print(i)
            elif button == '3':
                dir_name = input('Название папки для удаления: ')
                if dir_name in main_contents():
                    deleting_dirs(dir_name)
                    print('Папка %s успешно удалена ' % dir_name)
                else:
                    print('Невозможно удалить несуществующую папку %s' % dir_name)
            elif button == '4':
                path_dir = os.getcwd()
                dir_name = input('Создать папку: ')
                from os import path, chdir, getcwd, mkdir
                if not (path.exists(path_dir + '/' + dir_name)):
                    chdir(path_dir)
                    mkdir(dir_name)
                    print('Папка %s успешно создана' % dir_name)
                    # continue
                else:
                    print('Создание папки %s невозможно! Папка уже существует.' % dir_name)
            elif button == '5':
                print("Вы успешно вышли в главную директорию")    
                break
        except ValueError:
            print("Проверьте введенные данные")
        except SyntaxError:
            print("Проверьте синтаксис введенных данных")
        except OSError:
            print("Системная ошибка, обратитесь в ТехОтдел")


main_menu()