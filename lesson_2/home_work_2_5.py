rating = [7, 5, 3, 3, 2]

new_element = int(input('Пожалуйста введите новый элемент рейтинга: '))

counter = rating.count(new_element)  # проверяем есть ли эллемент в списке

# Если елемент есть добавляем его в конец таких же элементов, если нету, то просто добавляем и сортируем по убыванию
if counter:
    index = rating.index(new_element)
    rating.insert(index + counter, new_element)
else:
    rating.append(new_element)
    rating.sort(reverse=True)

print(rating)
