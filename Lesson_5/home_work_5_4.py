# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def translate(number: str):
    """Функция выполняет перевод английских числительных(до десяти) на русский"""
    number_translate = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                        "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    return number_translate[number.lower()].title()


try:
    with open("home_work_5_4(source).txt", "r", encoding='utf-8') as file:
        line_list = []
        for line in file:  # делаю так что бы избавиться от символа перевода на новую строку
            line_list.append(line.rstrip().split(" "))
        with open("home_work_5_4(result).txt", "w", encoding='utf-8') as f:
            for elem in line_list:
                f.write(f"{translate(elem[0])} - {elem[2]}\n")
except IOError as err:
    print(f"Произошла ошибка - {err}.")
