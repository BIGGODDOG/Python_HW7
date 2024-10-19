# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, area, price):
        self.area = area  
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __str__(self):
        return f"Квартира с площадью {self.area} м² и ценой {self.price} тг."

flat1 = Flat(34, 5000000) 
flat2 = Flat(53, 9000000)
flat3 = Flat(85, 25000000)

# Square comparison 
print(f"is flat1 == flat2? {flat1 == flat2}") 
print(f"is flat2 == flat3? {flat2 == flat3}") 
print(f"is flat2 != flat1? {flat2 != flat1}")  

# Price comparison
print(f"is flat1 > flat2? {flat1 > flat2}")
print(f"is flat1 < flat2? {flat1 < flat2}")  
print(f"is flat2 >= flat3? {flat2 >= flat3}") 
print(f"is flat1 <= flat3? {flat1 <= flat3}")  