list_of_str = input('Пожалуйста вводите слова через пробел\
 ,как закончите нажмите "ENTER": ').split()

for index, element in enumerate(list_of_str):
    if len(element) >= 10:
        element=element[0:10]
    print(index, element)