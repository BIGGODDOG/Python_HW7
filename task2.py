# Задание 2
# Создайте класс Complex (комплексное число).
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

class Complex:
    def __init__(self, real, imag):
        self.real = real  # Действительная часть
        self.imag = imag  # Мнимая часть

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real ** 2 + other.imag ** 2
            if denominator == 0:
                raise ZeroDivisionError("Ошибка: Деление на ноль невозможно")
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(3, 2)  # 3 + 2i
c2 = Complex(1, 7)  # 1 + 7i

c_add = c1 + c2
print(f"Сложение: {c_add}")  # (3 + 2i) + (1 + 7i) = 4 + 9i

c_sub = c1 - c2
print(f"Вычитание: {c_sub}")  # (3 + 2i) - (1 + 7i) = 2 - 5i

c_mul = c1 * c2
print(f"Умножение: {c_mul}")  # (3 + 2i) * (1 + 7i) = -11 + 23i

c_div = c1 / c2
print(f"Деление: {c_div}")  # (3 + 2i) / (1 + 7i) = 0.37 - 0.31i