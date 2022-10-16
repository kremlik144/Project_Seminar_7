# Модуль выполнения задач (1) и (2)

import controller
import view

# открытие родной базы самого приложения для считывания данных
def view_current_records():
    with open('directory_mode_1_2.txt', 'r', encoding="utf-8") as page:
        return page.readlines()

# добавление в справочник новой информации
def adding_new_entries():
    value = controller.entering_new_data()

    for i, values in enumerate(value):
        with open('directory_mode_1_2.txt', 'a', encoding="utf-8") as page:
            page.write(f'{values} \n')
        if i == 3:
            with open('directory_mode_1_2.txt', 'a', encoding="utf-8") as page:
                page.write('\n')

    view.progress_report()