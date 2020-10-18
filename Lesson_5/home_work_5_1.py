# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

print("Здравствуйте!")
with open("home_work_5_1.txt", "w", encoding='utf-8') as file:
    while True:
        user_text = input("Вводите что хотите: ")
        if len(user_text) == 0:
            break
        file.write(f"{user_text}\n")
if file.closed:
    print("Запись Произведена. Файл Закрыт!")
