# Написать класс треугольника
# конструктор - длины трех сторон
# методы проверить существование треугольника
# получить все углы треугольника

# Потренируюсь на прямоугольнике
class Rectangle:
    width = 12
    height = 50
    color = "red"
# Добавил метод считаем плозадь прямоугольника
# self - параметр, через который получим доступ к своим даным
    def square(self):
        return self.width * self.height

# Доступ к классу получу так
# имя_объекта. атрибут
rectan_1 = Rectangle()
print(rectan_1.width)
print(rectan_1.square()) # 600

#Метод – это функция находящаяся внутри класса,
# выполняющая определенную работу, которая, чаще всего,
# предполагает доступ к атрибутам созданного объекта.

# Конструктор класса задаем опред.
# параметры объекта при его создани. Т.е. возможность
# создавать объекты с уже заранее заданными атрибутами
# __init__(self)

# На примере прямоугольника
# задаем Класс:
#     опр.функцию __инит__(селф, цвет, ширина, высота):
#         селф.цвет = цвет
#         селф.ширина = ширина
#         селф.высота = высота
#
#     Функция
#         возвращает
#         свою.ширину * на свою.высоту

import math
# Первым параметром, как и у любого другого метода, у __init__ является self, на
# место которого подставляется объект в момент его создания. Второй и последующие
# параметры заменяются аргументами, переданными в "КОНСТРУКТОР" при вызове класса
class Triangle(object):
    def __init__(self, a = 2, b = 2, c = 10): # Типа если я тупо вызову - Вернет ошибку. А так не вернет.
        self.a = a
        self.b = b
        self.c = c

#defining class method
    def exists(self):
        if (self.a <= 0) or (self.b <= 0) or (self.c <= 0):
            return False
        if (self.a < self.b + self.c) and (self.b <= self.a + self.c) and (self.c <= self.a + self.b):
            return True
        if (self.a != self.b) or (self.a != self.c) or (self.b != self.c):
            print("Triangle with different sizes of sides")
        if (self.a == self.b) or (self.b == self.c):
            print("Triangle is equilateral")

    def get_angles(self):
        if not self.exists():
            return None
        if self.exists():
            cos_gamma = self._cos_triangle(self.a, self.b, self.c) #calling statimethod
            cos_beta = self._cos_triangle(self.a, self.b, self.c)
            cos_alpha = 180.0 - cos_beta - cos_gamma
            return cos_alpha, cos_beta, cos_gamma

 #No self parameter? Why
@staticmethod
def _cos_triangle(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2) / (2 * a * b)


#Create some object or instance
t_first = Triangle(2,3,0)
t_second = Triangle(2,2,2)
# t_second = Triangle(2,2,3) # error 'Triangle' object has no attribute '_cos_triangle'
t_third = Triangle()
t_fourth = Triangle(1,2,4)

print(t_second.exists())
# print(t_second.get_angles()) # None
print(t_third.get_angles()) # None
print(t_fourth.exists())