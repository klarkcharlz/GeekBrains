num = input('Пожалуйста введите число: ')

i = 1  #счетчик
max_number = num[0]

while i<len(num):
    if num[i]>max_number:
        max_number = num[i]
    i+=1
    
print(max_number)