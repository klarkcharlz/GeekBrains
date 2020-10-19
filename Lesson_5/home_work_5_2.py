# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    with open("home_work_5_2.txt", "r", encoding='utf-8') as file:
        num_line = {}
        i = 1  # счетчик строк
        for line in file:
            num_line[i] = len(line.split())
            i += 1
except IOError as err:
    print(f"Произошла ошибка - {err}.")
else:
    print(f"Всего строк {len(num_line)}.")
    for key in num_line:
        print(f"В строке {key} - {num_line[key]} слов.")
