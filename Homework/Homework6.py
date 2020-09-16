# Easy
# Задача 1
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

'''import os

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.
    Параметры:
        - a, b (int или float).
    Результат:
        - float.
    """
    return (a * b) ** 0.5


while True:
    try:

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(avg(a, b))
        print(c)

    except ValueError as ve:
        print(f"Ошибка: '{ve}! 'Это не число! Введите значение цифрами")
    except TypeError as te:
        print(f"Ошибка: {te} Невозможно определить среднее геометрическое"
              "\nвведенных чисел (а и b)."
              "\nВведенные числа должны быть либо положительыне,"
              "\nлибо отрицательные!")
    except Exception as ex:
        print("Ошибка:", ex)
    else:
        break'''


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
def creating_dirs(dir_name):
    """
    создание папки в текущей директории
    :param dir_name: название папки
    :return:
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(dir_path)


def deleting_dirs(dir_name):
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    :return:
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.rmdir(dir_path)


try:
    for i in range(9):
        name = 'dir_' + str(i + 1)
        creating_dirs(name)
        i += 1
except FileExistsError:
    print('Папки уже созданы')

    question = input('Хотите удалить папки (Да или Нет)?:')
    if question == 'Да':
            deleting_dirs(name)
    elif question == 'Нет':
        pass
    else:
        print('Введите Да или Нет!!!')


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
