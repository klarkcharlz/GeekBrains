list_of_number = list(map(int, input('Пожалуйста вводидите список чисел\
 через пробел, когда закончите нажмите "ENTER": ').split()))

for i in range(0, len(list_of_number), 2):
    if (i + 1) >= len(list_of_number):
        break
    temp = list_of_number[i]  # для хранения временного значения
    list_of_number[i] = list_of_number[i + 1]
    list_of_number[i + 1] = temp

print(list_of_number)
