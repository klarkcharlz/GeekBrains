# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    """Родительский класс"""
    def __init__(self, title:str):
        self.title = title
    def draw(self):
        print("Отрисовка.")


"""Дочерние классы"""

class Pen(Stationery):
    def __init__(self, title:str):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} рисует тонкими линиями.")

class Pencil(Stationery):
    def __init__(self, title:str):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} рсиует жирно и легко стирается ластиком. ")

class Handle(Stationery):
    def __init__(self, title:str):
        super().__init__(title)
    def draw(self):
        print(f"{self.title} рисует очень жирно.")


my_pen = Pen("Ручка")
my_pencil = Pencil("Карандаш")
my_handle = Handle("Маркер")

my_pen.draw()
my_pencil.draw()
my_handle.draw()
