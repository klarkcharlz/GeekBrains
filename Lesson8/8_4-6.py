# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.



class OfficeEquipment:
    """Класс оргтехника"""
    total_OfficeEquipment = 0
    def __init__(self, title:str, price:int, quantity:int):  # производитель, цена, количество
        self.technics_dict = {"title": title, "price": price, "quantity": quantity}
        OfficeEquipment.total_OfficeEquipment += quantity


class Printer(OfficeEquipment):
    """Класс принтер"""
    name = "Принтер"
    total_printer = 0
    def __init__(self, title:str, price:int, quantity:int, color:str, subdivision:str):  # + цвет, подразделение
        super().__init__(title, price, quantity)
        self.subdivision = subdivision
        self.technics_dict["color"] = color
        Printer.total_printer += quantity
    def acceptance(self, stock):  # передача товара на склад
        stock.acceptance_of_goods(self.subdivision, self.technics_dict,  self.name)


class Scanner(OfficeEquipment):
    """Класс сканер"""
    name = "Сканер"
    total_scanner = 0
    def __init__(self, title:str, price:int, quantity:int, resolution:str, subdivision:str):  # +разрешение печати
        super().__init__(title, price, quantity)
        self.subdivision = subdivision
        self.technics_dict["resolution"] = resolution
        Scanner.total_scanner += quantity
    def acceptance(self, stock):  # передача товара на склад
        stock.acceptance_of_goods(self.subdivision, self.technics_dict,  self.name)


class Copier(OfficeEquipment):
    """Класс ксерокс"""
    name = "Ксерокс"
    total_copier = 0
    def __init__(self, title:str, price:int, quantity:int, speed:int, subdivision:str):  # +скорость печати
        super().__init__(title, price, quantity)
        self.subdivision= subdivision
        self.technics_dict["speed"] = speed
        Copier.total_copier += quantity
    def acceptance(self, stock):  # передача товара на склад
        stock.acceptance_of_goods(self.subdivision, self.technics_dict,  self.name)


class Stock:
    """Класс склад"""
    def __init__(self, technics):
        self.total = technics.total_OfficeEquipment
    def __str__(self):
        print("Это класс содержащи информацию о всей оргтехнике хранящейся на специальном складе выделенном под неё.")
        return f"Всего техники на складе: {self.total}."
    def acceptance_of_goods(self, subdivision:str, technics_dict:dict, typ:str):  # прием товара на склад
        print(f"На склад на хранение для подразделения {subdivision}, пришло {technics_dict['quantity']} {typ}\
 производства {technics_dict['title']} по цене {technics_dict['price']} за одну штуку.")


class Validation:
    """Валидация пользовательского ввода"""
    @staticmethod
    def valid(typ, text):
        if typ == str:
            return input(text)
        if typ == int:
            while True:
                try:
                    num = int(input(text))
                except ValueError as err:
                    print(f"Вводите числа. {err}")
                else:
                    return num

print("Здравствуйте, Вас приетствует программа для сбора информации о технике поступающей на склад.")
print("Прием принтеров.")
# создадим экземпляры наших классов
my_printer = Printer(Validation.valid(str, "Производитель: "), Validation.valid(int, "Цена за одну штуку: "),
              Validation.valid(int, "Количество: "), Validation.valid(str, "Цветной или не цветной: "),
              Validation.valid(str, "Подразделение которому предназначается:"))
print("Прием сканеров.")
my_scanner = Scanner(Validation.valid(str, "Производитель: "), Validation.valid(int, "Цена за одну штуку: "),
              Validation.valid(int, "Количество: "), Validation.valid(str, "Разрешение: "),
              Validation.valid(str, "Подразделение которому предназначается:"))
print("Прием ксероксов.")
my_copier = Copier(Validation.valid(str, "Производитель: "), Validation.valid(int, "Цена за одну штуку: "),
              Validation.valid(int, "Количество: "), Validation.valid(int, "Скорость печати в минуту: "),
              Validation.valid(str, "Подразделение которому предназначается:"))

# создадим склад под технику
my_stock = Stock(OfficeEquipment)

# отправим технику на склад
my_copier.acceptance(my_stock)
my_scanner.acceptance(my_stock)
my_printer.acceptance(my_stock)

# посмотрим сколько всего техники мы храним
print(my_stock)