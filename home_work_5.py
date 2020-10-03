proceeds = int(input('Введите пожалуйста выручку вашей фирмы: '))
costs = int(input('Введите пожалуйста издержку вашей фирмы: '))

if proceeds>costs:
    profit = proceeds - costs #Прибыль фирмы, выручка минус затраты
    profitability = round(profit/proceeds,2) #Реентабельность
    print('Ваша фирма прибыльна!')
    print('Реентабельность вашей фирмы составляет: %0.2f .' %profitability)
    working = int(input('Сколько сотрудников трудится в вашей фирме? '))
    profit_working = round(profit/working,2)
    print('Прибыль на одного сотрудника составляет: %0.2f .' %profit_working)
elif proceeds==costs:
    print('Ваша фирма вышла в 0!')
else:
    print('Увы, но Ваша фирма терпит убытки!')