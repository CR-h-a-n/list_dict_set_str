indicator = False   # Указатель введено ли число
while indicator == False:
    number_elements = input('Введите количество элементов: ')
    if number_elements.isnumeric():
        number_elements = int(number_elements)
        indicator = True
    else:
        print('Введите коррекное значение.')

list_elements = []
for i in range(number_elements):
    indicator = False     # Указатель введено ли число
    while indicator == False:
        element = input('Введите элемент №'+ str(i+1) + ': ')
        if element.isnumeric():
            indicator = True
            list_elements.append(int(element))
        else:
            print('Введите коррекное значение.')

list_elements.sort()

print('Вывод: ', end=' ')
for i in range(number_elements):
    if i == number_elements - 1:
        print(list_elements[i])
    else:
        print(list_elements[i], end=', ')