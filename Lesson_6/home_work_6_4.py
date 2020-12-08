# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    """Родительский класс"""
    def __init__(self, speed:float, color:str, name:str, is_police:bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.prefix = 'Полицейская' if is_police else ''
    def show_speed(self):
        print(f"Ваша скорсоть составляет: {self.speed} км/ч.")
    def go(self):
        print(f"{self.prefix} {self.color} {self.name} поехала.")
    def stop(self):
        print(f"{self.prefix} {self.color} {self.name} остановилась.")
    def turn(self, direction:str ):
        print(f"{self.prefix} {self.color} {self.name} повернула на {direction}.")


"""Дочерние классы"""

class TownCar(Car):
    speed_limit = 60
    def __init__(self, speed:float, color:str, name:str, is_police:bool):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed >= self.speed_limit:
            print(f"Внимание Вы превысили допустимую скорость {self.speed_limit} км в час!\
 Ваша скорсоть составляет: {self.speed}км/ч.")
        else:
            print(f"Ваша скорсоть составляет: {self.speed} км/ч.")


class WorkCar(Car):
    speed_limit = 40
    def __init__(self, speed:float, color:str, name:str, is_police:bool):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed >= self.speed_limit:
            print(f"Внимание Вы превысили допустимую скорость {self.speed_limit} км в час!\
 Ваша скорсоть составляет: {self.speed}км/ч.")
        else:
            print(f"Ваша скорсоть составляет: {self.speed} км/ч.")


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


# создание экзмепляров класса
niva = TownCar(50.4, "Черная", "Нива", False)
gazele = WorkCar(45.3, "Белая", "Газель", False)
polize = PoliceCar(120.9, "Синяя", "Рено", True)

# вызов атрибутов
print(f"Атрибуты экземпляра {niva}: {niva.name}, {niva.color}, {niva.speed}, {niva.is_police}.")
print(f"Атрибуты экземпляра {gazele}: {gazele.name}, {gazele.color}, {gazele.speed}, {gazele.is_police}.")
print(f"Атрибуты экземпляра {polize}: {polize.name}, {polize.color}, {polize.speed}, {polize.is_police}.")

# вызов методов
niva.go()
niva.show_speed()
niva.turn("лево")
niva.stop()

gazele.go()
gazele.show_speed()
gazele.turn("право")
gazele.stop()

polize.go()
polize.show_speed()
polize.turn("верх")
polize.stop()
