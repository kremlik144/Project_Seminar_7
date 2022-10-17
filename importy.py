# Модуль операции (4)

import controller
import view
import time


# проверка формата данный и имени импортируемого файла 
def contacts_import(name):
    try:
        with open(f'{name}.txt', 'r', encoding="utf-8") as page:
            import_value = page.readlines()
            if controller.format_check(import_value):
                with open(f'directory_mode_1_2.txt', 'a', encoding="utf-8") as page:
                        for i in import_value:
                            page.write(i)
                                  
    except:
        print('\nВы не добавили импортируемый файл в папку проекта!'
              'Прочтите еще раз инструкцию режима (4) !' )
        time.sleep(3)
        controller.distribution_by_modes(4)
    return True
    


def contacts_import_2(lst):
    print(lst)

'''принимает список из списков контактов, отфильтрованный, готовый к записи в само приложение 
осталось только разделить по элементам и придумать как записать'''

