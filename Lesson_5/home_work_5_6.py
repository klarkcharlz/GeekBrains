# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

def counter(sub_list: list):
    num_list = []
    for elem in sub_list:
        num = ""
        for el in elem:
            if el.isdigit():
                num += el
        if len(num):
            num_list.append(int(num))
    return sum(num_list)


subject_dict = {}
try:
    with open("home_work_5_6.txt", "r", encoding='utf-8') as file:
        personal_list = []
        for line in file:  # делаю так что бы избавиться от символа перевода на новую строку
            personal_list.append(line.rstrip().split())
        for elem in personal_list:
            subject_dict[elem[0].replace(":", "")] = counter(elem[1:])
except IOError as err:
    print(f"Произошла ошибка - {err}.")
else:
    for key in subject_dict:
        print(f"Общее количество занятий по предмету - {key} составляет : {subject_dict[key]}.")
