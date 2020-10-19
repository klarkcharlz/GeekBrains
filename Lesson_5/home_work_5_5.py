# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.

import random

with open("home_work_5_5.txt", "w", encoding='utf-8') as file:
    i = 0
    while i < 100:
        file.write(f"{str(random.randint(1, 100))} ")
        i += 1
try:
    with open("home_work_5_5.txt", "r", encoding='utf-8') as file:
        number_list = list(map(int, file.read().split()))
except IOError as err:
    print(f"Произошла ошибка - {err}.")
else:
    print(f"Сумма всех эллементов равна: {sum(number_list)}.")
