# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). 
# Данные методы должны применяться только к клетками
# и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. 
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    """Класс клетка"""
    def __init__(self, n:int):
        """Иницииализатор класса, принимает количество ячеек клетки"""
        self.n = n
        
    def __str__(self):
        """преобразует объект к строке"""
        return f"Количество ячеек новой клетки равно: {self.n}."
    
    def __add__(self, other):
        """ "Магический метод" - сложение"""
        return Cell(self.n + other.n)
    
    def __sub__(self, other):
        """ "Магический метод" - вычитание"""
        if self.n - other.n <= 0:
            return "Разность меньше нуля!"
        else:
            return Cell(self.n - other.n)
        
    def __mul__(self, other):
        """ "Магический метод" - умножение"""
        return Cell(self.n  * other.n)
    
    def __truediv__(self, other):
        """ "Магический метод" - деление"""
        return Cell(self.n // other.n)    
    
    def make_order(self, number_in_row:int):
        """
        Формирует строку вида вида *****\n*****\n*****
        где количество ячеек между \n равно переданному аргументу -number_in_row 
        """
        self.n -= number_in_row
        string = r""
        while self.n > 0:
            self.n -= number_in_row
            string += r"*" * number_in_row + r"\n"
        else:
            number_in_row += self.n
            string += r"*" * number_in_row
        return string

# Создание экземпляров класса
my_cell = Cell(12)
you_cell = Cell(15) 

# Проверка перегрузки операторов
print(my_cell + you_cell)
print(my_cell - you_cell)
print(you_cell - my_cell)
print(you_cell * my_cell)
print(you_cell / my_cell)
print(my_cell / you_cell)

# Вызов метода атрибутов класса
print(my_cell.make_order(5))
print(you_cell.make_order(5))
    