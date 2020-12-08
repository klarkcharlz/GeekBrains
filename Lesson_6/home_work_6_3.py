# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    """Родительский класс"""
    def __init__(self, name:str, surname:str, position:str, wage:int, bonus:int):
        self.name = name
        self.surname = surname
        self.position = position
        _income= {"wage":wage, "bonus":bonus}
    def show_income(self):
        print(self._income)


class Position(Worker):
    """Дочерний класс"""
    def __init__(self, name:str, surname:str, position:str, wage:int, bonus:int):
        super().__init__(name, surname, position, wage, bonus)
        self._income= {"wage":wage, "bonus":bonus}
    def get_full_name(self):
        print(f"Имя и фамилия сотрудника: {self.name} {self.surname}.")
    def get_total_income(self):
        print(f"Доход сотрудника на должности {self.position}  составляет: {self._income['wage'] + self._income['bonus']}.")


python_developer = Position("Николай", "Петров", "Питон разработчик", 180_000, 120_000)
python_developer.get_full_name()
python_developer.get_total_income()

c_plus_plus_developer = Position("Ник", "Николсон", "C++ разработчик", 70_000, 20_000)
c_plus_plus_developer.get_full_name()
c_plus_plus_developer.get_total_income()
# проверка переменных
print(python_developer.name)
print(python_developer.surname)
python_developer.show_income()

print(c_plus_plus_developer.name)
print(c_plus_plus_developer.surname)
c_plus_plus_developer.show_income()
