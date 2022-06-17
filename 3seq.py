def input_my_list(count_list): # Функция ввода списка
    indicator = False  # Указатель введено ли число
    while indicator == False:
        number_elements = input('Введите количество элементов списка №' + str(count_list) + ': ')
        if number_elements.isnumeric():
            number_elements = int(number_elements)
            indicator = True
        else:
            print('Введите коррекное значение.')

    list_elements = []
    for i in range(number_elements):
        indicator = False  # Указатель введено ли число
        while indicator == False:
            element = input('Введите элемент №' + str(i + 1) + ': ')
            if element.isnumeric():
                indicator = True
                list_elements.append(int(element))
            else:
                print('Введите коррекное значение.')
    return(list_elements)


def output_my_list(list_elements, count_list): # Вывод списка
    print('Список №' + str(count_list) + ':', end=' ')
    number_elements = len(list_elements) # Количество элементов списка
    if number_elements != 0:
        for i in range(number_elements):
            if i == number_elements - 1:
                print(list_elements[i])
            else:
                print(list_elements[i], end=', ')
    else:
        print()

my_list1 = []
my_list1 = input_my_list(1)
my_list2 = []
my_list2 = input_my_list(2)

output_my_list(my_list1, 1)
output_my_list(my_list2, 2)

for count_my_list2 in range(len(my_list2)): # Перебор элементов второго списка
    for count_overlap in range(my_list1.count(my_list2[count_my_list2])): # Удаление из первого списка элемента из второго списка
        my_list1.remove(my_list2[count_my_list2])                         # столько раз, сколько посчитает метод count

print()
print('Результат: ')
output_my_list(my_list1, 1)