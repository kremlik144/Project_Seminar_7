# Модуль контроля процессов 

import view as mode
import view_and_add as v_a_a
import export


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
        if mod[0] == True: export.asd(information, mod[1])


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


# проверка ввода режима (3) и (4)
def mode_check(value, mod = 3):
    while value not in ['1', '2']:
        print('\n\tВведите корректное значение!\n ')
        if mod == 3: value = mode.export_format()
        if mod == 4: pass #для 4 режима
    return True, value


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