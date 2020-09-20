import os

def creating_dirs(path_dir, dir_name):
    """
    создание папки в текущей директории
    :param path_dir: путь текущей директории
    :param dir_name: название папки
    :return:
    """
    if not (path.exists(path_dir + '/' + dir_name)):
        chdir(path_dir)
        mkdir(dir_name)
    else:
        print('Создание папки %s невозможно! Папка уже существует.' % dir_name)


def deleting_dirs(dir_name):
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    :return:
    """
    from os import path, getcwd, rmdir
    try:
        dir_path = path.join(getcwd(), dir_name)
        rmdir(dir_path)
    except FileExistsError:
        print(f'Создание уже существующей папки \'{dir_name}\' невозможно')


def main_contents():
    """
    выводит содержание папки по заданному пути
    :param specified_path: заданный путь
    :return:
    """
    from os import listdir, getcwd
    return listdir(getcwd())
    


