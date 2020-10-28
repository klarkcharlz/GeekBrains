# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re

class ValidFail(Exception):
    def __init__(self, text):
        self.text = text

class DateError(Exception):
    def __init__(self, text):
        self.text = text

class Date_time:
    """Класс дата"""
    day = None
    month = None
    year = None
    def __init__(self, date:str):
        self.day, self.month, self.year = self.date_init(date)

    @classmethod
    def date_init(cls, date:str):
        """метод проверяет корректность ввода даты и преобразует ее в int"""
        date_regex = re.compile(r"\d+")
        date_list = list(map(int, date_regex.findall(date)))
        try:
            if len(date_list) > 3  or len(date_list) < 3:
                raise DateError("Неправильный формат даты.")
            if cls.valid(date_list):
                return date_list
            else:
                raise ValidFail("Числа выходят за допустимые диапазоны.")
        except DateError as err:
            print(err.text)
        except ValidFail as err:
            print(err.text)
        if ValidFail or DateError:  # в случае возникновения исключений вернем None, как поступить лучше незнаю
            return [None, None, None]

    @staticmethod  # не имеет доступа к атрибутам класса и экземпляров класса
    def valid(date:list):
        """метод проверяет попадание даты в допустимый диапазон"""
        if 1 <= date[0] <= 31 and 1 <= date[1] <= 12 and 1 <= date[2] <= 2020:
            return True
        else:
            return False

    def __str__(self):
        if self.day and self.month and self.year:
            return f"{self.day:02}:{self.month:02}:{self.year:04}"
        else:
            return "Вы ввели некоректные данные."

# вызываем classmethod через класс, + с вариантами ошибок
print(Date_time.date_init("21-04-1992"))  # -> [21, 4, 1992]
print(Date_time.date_init("21-04-19924"))  # -> Числа выходят за допустимые диапазоны. [None, None, None]
print(Date_time.date_init("21-04-1992-2")) # -> Неправильный формат даты. [None, None, None]
# вызываем staticmethod через класс
print(Date_time.valid([21, 4, 1992]))  # -> True

# создаем экземпляр класса и проверим вывод даты
my_date = Date_time("21-04-1992")
print(my_date)  # -> 21:04:1992
# обратимся отдельно к classmethod и staticmethod через экземпляр класса
print(my_date.date_init("21-04-1992"))  # -> [21, 4, 1992]
print(my_date.valid([21, 4, 1992]))  # -> True

