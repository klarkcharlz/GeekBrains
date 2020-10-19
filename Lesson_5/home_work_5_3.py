# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

try:
    with open("home_work_5_3.txt", "r", encoding='utf-8') as file:
        personal_list = []
        summa = 0  # для подсчета среднего оклада
        for line in file:  # делаю так что бы избавиться от символа перевода на новую строку
            personal_list.append(line.rstrip())
        for elem in personal_list:
            salary = float(elem.split()[1])
            summa += salary
            if salary < 20000:
                print(f"У {elem.split()[0]} оклад менее 20 тыс, а именно {salary}.")
except IOError as err:
    print(f"Произошла ошибка - {err}.")
else:
    print(f"Средний оклад всех сотрудников составляет: {summa/len(personal_list)}.")
