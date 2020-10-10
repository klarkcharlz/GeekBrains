#Реализовать функцию, принимающую два числа 
#(позиционные аргументы) и выполняющую их деление. 
#Числа запрашивать у пользователя, 
#предусмотреть обработку ситуации деления на ноль.

def division(num_one:float, num_two:float):
    """Функция принимает два числа и вовращает результат деления первого 
    на второе"""
    try:
         result = num_one / num_two
    except ZeroDivisionError:
        print("На ноль делить нельзя!!!")
    else:
        print(f"В результате деления {num_one} на {num_two}\
 будет {result}.")

while True:
    print("Здравствуйте, Вас приветствует программа реализующая\
 деление чисел. Но помните, на 0 делить нельзя!")
    try: 
        num_one = float(input("Введите пожалуйста первое число: "))
        num_two = float(input("Введите пожалуйста второе число: "))   
    except ValueError:
        print("Пожалуйста вводите числа!!!")
    else:
        division(num_one, num_two)
        break
