# Задания после урока № 1.

# Cложное задание(нет).

a = float('inf')

print (a == a**2) 

print (a == a*2)

print (a > 9999999999) 

# Задание 1 - возраст.

name = 'Виктор'

name2 = 'Олег'

age = (27)

age2 = (18)

age3 = str(age - age2)

print (name +" на "+ age3 +" лет старше чем "+ name2 +" которому  "+ str(age2))

# Задание 2 - поменять местами.

a = input("Введите первое число: ")

b = input("введите второе число: ")

c = input("введите третье число: ")

a, b, c = c, b, a

print("Теперь первое число: ", a)

print("Теперь второе число: ", b)

print("Теперь третье число: ", c)

# Задание 3 - найти дискриминант.

import math

print('ax2 + bx + c = 0') # для наглядности.

print('D = b ** 2 - 4 * a * c') # для наглядности 2.

a = int(input("Введите значение: a = "))

b = int(input("Введите значение: b = "))

c = int(input("Введите значение: c = "))

D = b ** 2 - 4 * a * c

print(D)

if D < 0:

  print("Корней нет")

elif D == 0:

  x = -b / (2 * a)

  print (x)

else:

  x1 = (-b + math.sqrt(D)) / (2 * a)

  x2 = (-b - math.sqrt(D)) / (2 * a)

  print(x1)

  print(x2)
