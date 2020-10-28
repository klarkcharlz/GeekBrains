#Реализовать формирование списка, используя функцию range() 
#и возможности генератора. В список должны войти четные числа от 100 до 1000 
#(включая границы). 
#Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce

def multiplication(num_1:int, num_2:int):
    return num_1 * num_2

my_list = [num for num in range(100, 1001) if num % 2 == 0]

print(reduce(multiplication, my_list))
