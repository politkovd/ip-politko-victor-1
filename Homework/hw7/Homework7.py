# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangl:
        """ класс треугольника"""

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

            a = 5
            b = 5
            c = 5

            d = (a + b)*c

            print(d)

        # def plosh(self):
            
            

        #     self.d = (self.a + self.b) * self.c

        # print(Triangl.plosh(self))
         

            

            


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
