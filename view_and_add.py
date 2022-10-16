import controller
import view

# открытие родной базы самого приложения для считывания данных
def view_current_records():
    with open('directory_mode_1.txt', 'r', encoding="utf-8") as page:
        return page.readlines()

# добавление в базу приложения новой информации
def adding_new_entries():
    value = controller.entering_new_data()

    for i, values in enumerate(value):
        with open('directory_mode_1.txt', 'a', encoding="utf-8") as page:
            page.write(f'{values} \n')
        if i == 3:
            with open('directory_mode_1.txt', 'a', encoding="utf-8") as page:
                page.write('\n')

    view.progress_report()