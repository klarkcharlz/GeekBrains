struct = []
i = 1  # счетчик
n = int(input('Здравствуйте! Информацию о скольки товарах Вы хотите заполнить?'))
while n > 0:
    """Помещаем вводимые данные в словарь, словарь в кортеж, а кортеж в список"""
    tuple_to_add = []  # Словарь который будем преобразовывать в кортеж
    dict_of_products = {'Наименование': input(f'Введите наименование товара №{i}: '),
                        'Цена': int(input(f'Введите цену товара №{i}: ')),
                        'Количество': int(input(f'Введите количество товара №{i}: ')),
                        'Ед.': input(f'Введите еденицу измерения количества товара №{i}: ')}
    tuple_to_add.append(i)
    tuple_to_add.append(dict_of_products)
    struct.append(tuple(tuple_to_add))
    i += 1
    n -= 1

print(struct)

products = {'Наименование': [], 'Цена': [], 'Количество': [], 'Ед.': []}

for elem in struct:
    for el in elem:
        if type(el) == dict:
            for key in el:
                products[key].append(el[key])

print(products)
