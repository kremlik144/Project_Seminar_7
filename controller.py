# Модуль контроля процессов 

import view as mode
import view_and_add as v_a_a
import export
import importy


# контоль ввода корректного значения режима работы приложения
def operating_mod_check():
    value = mode.working_mode()
    while value not in ['1', '2', '3', '4']:
        print('\n\tВведите корректное значение!\n ')
        value = mode.working_mode()
    distribution_by_modes(int(value))


# разделение на режимы работы
def distribution_by_modes(mode_number):
    if mode_number == 1:
        result = v_a_a.view_current_records()
        mode.print_mode_1(result)
    elif mode_number == 2:
        result = v_a_a.adding_new_entries()
    elif mode_number == 3:
        information = v_a_a.view_current_records()
        value = mode.export_format()
        mod = mode_check(value)
        if mod[0] == True: export.contacts_export(information, mod[1])
    elif mode_number == 4:
        value = mode.import_format()
        name = name_check(value)
        flag = importy.contacts_import(name)
        if flag: mode.progress_import(name)


# проверка ввода новых записей режима (2)
def entering_new_data():
    categories = ['Фамилия', 'Имя', 'Номер телефона', 'Описание' ]
    new_contact = []
    print()
    for i in categories:
        while True:
            value = input(f'{i} нового контакта: ')
            if value.isalpha() and i != 'Номер телефона':
                new_contact.append(value.capitalize())
                break
            elif i == 'Номер телефона' and value.isdigit():
                new_contact.append(value)
                break
            else: print(f'\nВведите корректное значение "{i}"!\n')

    return new_contact


# проверка ввода режима (3)
def mode_check(value, mod = 3):
    while value not in ['1', '2']:
        print('\n\tВведите корректное значение!\n ')
        if mod == 3: value = mode.export_format()
    return True, int(value)


# проверка имени файла из режима (3) и (4)
def name_check(name):
    while True:
        if name.isalnum():
            return name
        else: 
            print(f'\nВведите корректное название файла! Без пробелов, '
            'используя только буквы и цифры.\n')
            name = input('\nВведите имя файла: ')


# проверка формата импортируемого файла (4)
def format_check(lst):
    order_counter = 1
    end_counter = 0

    # проверка на формат через пустую строку
    if '***' not in lst[0]:
        for value in lst:
            if order_counter in [1, 2, 4] and '\n' in value:
                if value[:-1].isalpha():
                    order_counter += 1
            elif order_counter == 3 and '\n' in value:
                if value[:-1].isdigit():
                    order_counter += 1
            elif order_counter == 5 and value == '\n':
                end_counter += order_counter
                order_counter = 1  

        if end_counter == len(lst): return True
        else: mode.eror_format()
        
    # проверка на формат через ***
    elif '***'  in lst[0]:
        end_counter_flag = 0
        new_lst = []

        for value in lst:
            result_lst = value[:-1].split('***')
            new_lst.append(result_lst)
            count_flag = 0
            
            for value_ in result_lst:
                if count_flag in [0, 1, 3]:
                    if value_.isalpha(): count_flag += 1
                elif count_flag == 2:
                    if value_.isdigit(): count_flag += 1
            if count_flag == 4: end_counter_flag += 1

        if end_counter_flag == len(lst): importy.contacts_import_2(new_lst)
        else: mode.eror_format() 


# работа приложения до тех пор пока хочет пользователь 
def duration_of_work():
    while True:
        value = input('Хотите продолжить? Введите (Yes) или (No): ')
        if value.capitalize() == 'Yes':
            operating_mod_check()
            break
        elif value.capitalize() == 'No': 
            print('Пока :)')
            break
        else: print('Введите Yes или No :)')