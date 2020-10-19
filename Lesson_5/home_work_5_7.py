# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

try:
    with open("home_work_5_7.txt", "r", encoding='utf-8') as file:
        count = 0  # счетчик фирм отработавших в плюс
        summa = 0  # для подсчета средней прибыли
        firm_list = []
        firm_dict = {}
        average_dict = {}
        lesion_firm = {}  # убыточные фирмы
        for line in file:  # делаю так что бы избавиться от символа перевода на новую строку
            firm_list.append(line.rstrip().split())
        print("Прибыль фирм: ")
        for firm in firm_list:
            profit = int(firm[2]) - int(firm[3])
            print(f"Прибыль фирмы {firm[1]} {firm[0]} составляет {profit}.")
            if profit > 0:
                firm_dict[firm[0]] = profit
                summa += profit
                count += 1
            else:
                lesion_firm[firm[0]] = profit
        average_dict["average_profit"] = summa/count
        print(f"Средняя прибыль среди {count} фирм отработавших в плюс состалвляет: {average_dict['average_profit']}.")
        json_list = [firm_dict, average_dict, lesion_firm]
        with open("home_work_5_7.json", "w", encoding='utf-8') as f:
            json.dump(json_list, f)
except IOError as err:
    print(f"Произошла ошибка - {err}.")
else:
    print(f"Запись JSON в файл произведена {json_list}.")
