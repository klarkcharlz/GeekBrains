# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
import re

def counter(sub_list: list):
    """Функция подсчитывает и возвращает общее количество уроков по предмету"""
    text = " ".join(sub_list)
    lesson_regex = re.compile(r"\d+")
    lesson = lesson_regex.findall(text)
    return sum(list(map(int,lesson)))

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
