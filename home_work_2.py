sec = int(input('Введите пожалуйста количество секунд: '))
hours = sec//3600
minutes = sec%3600//60
seconds = sec%60
print('%d:%02d:%02d' %(hours,minutes,seconds))