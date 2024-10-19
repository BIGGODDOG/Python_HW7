# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Ошибка: Радиус должен быть положительным числом")
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)) and value > 0:
            return Circle(self.radius + value)
        raise ValueError("Ошибка: Значение должно быть положительным числом.")

    def __sub__(self, value):
        if isinstance(value, (int, float)) and 0 < value < self.radius:
            return Circle(self.radius - value)
        raise ValueError("Ошибка: Значение должно быть положительным числом и меньше текущего радиуса.")

    def __iadd__(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.radius += value
            return self
        raise ValueError("Ошибка: Значение должно быть положительным числом.")

    def __isub__(self, value):
        if isinstance(value, (int, float)) and 0 < value < self.radius:
            self.radius -= value
            return self
        raise ValueError("Ошибка: Значение должно быть положительным числом и меньше текущего радиуса.")

    def __str__(self):
        return f"Окружность с радиусом: {self.radius}, длина окружности: {self.circumference():.2f}"

circle1 = Circle(2)
circle2 = Circle(3)

print(f"is circle1 equal to circle2? {circle1 == circle2}")  # False

print(f"is circle1 < circle2? {circle1 < circle2}")   # True
print(f"is circle1 >= circle2? {circle1 >= circle2}")  # False

circle3 = circle1 + 3
print(circle3)  

circle4 = circle2 - 2
print(circle4) 

circle1 += 2
print(circle1) 

circle2 -= 1
print(circle2) 