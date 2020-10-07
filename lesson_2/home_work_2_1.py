list_of_types = [3, 5.34, 'Строка из слов', True, ['Список', 'списков'],
                 ('Это', 'кортеж'), {'это': 'словарь'},
                 {1, 2, 3}, b'text']

for elements in list_of_types:
    print(f'{elements} is {type(elements)}')
