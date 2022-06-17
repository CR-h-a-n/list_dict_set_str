print('Допускается использовать: "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"')
print('Для разделения чисел используйте один из знаков: "," или ";" или "/"')
print('-' * 50)

input_pointer = False
while input_pointer == False:
    enter_data = input('Введите целые числа через разделитель: ')
    len_enter_data = len(enter_data)
    separator = ''
   #for i in range(len_enter_data):
    i = 0
    while i < len_enter_data:
        element = enter_data[i]
        if element in ('0','1','2','3','4','5','6','7','8','9',',',';','/'):
            if element in (',',';','/'):
                if separator == '':
                    separator = element   # Запомнили первый разделитель
                    input_pointer = True
                else:
                    if separator != element: # Если встретили другой разделитель
                        print('Вы используете несколько разделителей.')
                        print('Для разделения чисел используйте один из знаков: "," или ";" или "/"')
                        print('-' * 50)
                        input_pointer = False
                        i = len_enter_data
                    else:
                        input_pointer = True
            else:
                input_pointer = True
        else:
            print('Вы используете недопустимое значение: "' + element + '"')
            print('Допускается использовать цифры: "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"')
            print('Для разделения чисел используйте один из знаков: "," или ";" или "/"')
            print('-' * 50)
            input_pointer = False
            i = len_enter_data

        i += 1


my_list = []
if separator != '': # Если были разбиты цифры одним из разделителей
    my_list = enter_data.split(separator) # Разбили полученный список на элементы
    my_list = set(my_list)  # Преобразовали список в множество, оставив уникальные значения
    my_list = list(my_list) # Преобразовали множество обратно в список

    # Если при вводе между разделителями не ввели число (пример",,")
    # или вводимое значение начинается/заканчивается на разделитель,
    # то в списке есть пустое значение - убираем его
    if my_list.count('') != 0:
        my_list.remove('')

else:
    my_list.append(int(enter_data)) # Введено одно число


print('Вывод: ', end=' ')
len_my_list = len(my_list)
for i in range(len_my_list):
    if i == len_my_list - 1:
        print(my_list[i])
    else:
        print(my_list[i], end=', ')