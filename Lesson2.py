# Урок 1
# Логические операции
# > больше, < меньше, == равно, != не равно, >= больше или равно, <= меньше или равно

# x = 5 > 10
#
# type(x)
#
# print(x)
# print(type(x))

#Ветвление
# x = int(input('Введите число'))
# print(x)
# if x != 1:
#     print('yes')
# elif x == 2:
#     print('no')
# else:
#     print('ALARM')

#Пример

# original_password = 'x777'
#
# reserved_pass = '00000'
#
# password = input('Введите пароль:')
#
# if password == original_password:
#
#     print('Пароль правильный, добро пожаловать в систему')
#
# elif password == reserved_pass:
#
#     print('Пароль правильный, добро пожаловать в систему')
#
# else:
#     print('Пароль не верен, вход запрещен')

# Пример2

# x = 1
# print(x)
# if x == 1:
#     print('yes')
#     x = 'False'
#     x = False
#     x = ''
#     x =  0
#     if x:
#         print('Yahoo')
#     else:
#         print('Why?')
# else:
#     print('NO')

# Пример 3

# color = 'red'
# if color == 'blue':
#     print('Синий')
# elif color == 'red':
#     print('красный')
# elif color == 'green':
#     print('зеленый')
# else:
#     print('неизвестный цвет')

#  Знакомство с циклами
#
# a = 0
# while a < 7:
#      print('1')
#      a += 1
#
# x = input('Say yes or no:')
# while x == 'yes':
#     x = input('Say yes or no:')
# print('YEES')

#  Пример 4

# a = 6
# while a >= 0:
#     if a == 7:
#         break
#     a += 1
#     print("A")

# a = -1
# while a < 10:
#         a += 1
#         if a == 7 or a % 2 == 0:
#             continue
#         print('a--', a)

# a = 5
# while a > 0:
#     print("!")
#     break
#     a = a+1


# Цикл For

# word_str = "Hello, word!"
# i = 0
# for m in word_str:
#
#     if m == 'l':
#         i = i+1
#     if i == 2:
#         print(m)
#         break
#     print(m)
#
# lst = [1,3,5,7,9]
# for i in lst:
#     print(i**2)