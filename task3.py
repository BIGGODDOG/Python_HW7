# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).

class Airplane:
    def __init__(self, plane_type, max_passengers, current_passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.plane_type == other.plane_type
        return NotImplemented

    def __add__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passenger_count = self.current_passengers + passengers
            if new_passenger_count <= self.max_passengers:
                return Airplane(self.plane_type, self.max_passengers, new_passenger_count)
            else:
                raise ValueError("Ошибка: Число пассажиров превышает максимальную вместимость")
        return NotImplemented

    def __sub__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passenger_count = self.current_passengers - passengers
            if new_passenger_count >= 0:
                return Airplane(self.plane_type, self.max_passengers, new_passenger_count)
            else:
                raise ValueError("Ошибка: Число пассажиров не может быть отрицательным")
        return NotImplemented

    # Перегрузка операторов "+=" и "-=": добавление и удаление пассажиров in-place
    def __iadd__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passenger_count = self.current_passengers + passengers
            if new_passenger_count <= self.max_passengers:
                self.current_passengers = new_passenger_count
                return self
            else:
                raise ValueError("Ошибка: Число пассажиров превышает максимальную вместимость")
        return NotImplemented

    def __isub__(self, passengers):
        if isinstance(passengers, int) and passengers > 0:
            new_passenger_count = self.current_passengers - passengers
            if new_passenger_count >= 0:
                self.current_passengers = new_passenger_count
                return self
            else:
                raise ValueError("Ошибка: Число пассажиров не может быть отрицательным")
        return NotImplemented

    # Перегрузка операторов для сравнения по максимально возможному числу пассажиров
    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __str__(self):
        return (f"Самолет {self.plane_type}: "
                f"максимум пассажиров {self.max_passengers}, "
                f"текущих пассажиров {self.current_passengers}")

plane1 = Airplane("Boeing 777", 453, 125)
plane2 = Airplane("Concord", 205, 189)

print(f"is plane1 == plane2? {plane1 == plane2}")  # False

plane1 += 50  # Увеличение пассажиров на 50
print(plane1)  

plane2 -= 30  # Уменьшение пассажиров на 30
print(plane2)  

# Сравнение самолетов по максимальной вместимости
print(f"is plane1 > plane2? {plane1 > plane2}")  # True
print(f"is plane1 <= plane2? {plane1 <= plane2}")  # False