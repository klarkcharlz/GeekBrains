# Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно. 
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. 
# Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, 
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    rate = 0  # Расход
    """Основной класс Одежда"""
    def __init__(self, title:str):
        self.title = title
        
    @abstractmethod
    def consumption(self):
        """определения расхода ткани"""
        pass


# дочерние классы
class Coat(Clothes):
    """Класс пальто"""
    def __init__(self, title:str, V:int):
        super().__init__(title)
        self.V = V
    
    @property
    def consumption(self):
        """определения расхода ткани"""
        self.rate = round((self.V / 6.5) + 0.5)
        return self.rate

    def __add__(self, other):
        """Для расчета общего расхода"""
        return self.rate + other.rate

    
class Suit(Clothes):
    """Класс костюм"""
    def __init__(self, title:str, H:int):
        super().__init__(title)
        self.H = H
        
    @property
    def consumption(self):
        """определения расхода ткани"""
        self.rate = round((2 * self.H) + 0.3)
        return self.rate

    def __add__(self, other):
        """Для расчета общего расхода"""
        return self.rate + other.rate


# Создание экземпляров классов
my_coat = Coat("Дорогое пальто", 64)
my_suit = Suit("Дешевый костюм", 184)

"""Проверка вызова методов классов при использовании декоратора @property
что позволяет нам обращаться  методу как к атрибуту класса. """
print(f"Расход на производство {my_coat.title} составляет {my_coat.consumption}.")
print(f"Расход на производство {my_suit.title} составляет {my_suit.consumption}.")

# общий расход
print(f"Общий рас ход на производство {my_coat.title} и {my_suit.title} составляет {my_coat + my_suit}.")



