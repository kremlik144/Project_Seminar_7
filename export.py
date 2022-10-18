# Модуль операции (3)

import view

# запрашивает имя создаваемого файла, и передает данные на запись в соответствии с режимом
def contacts_export(lst, mod):
    name_new_file = view.file_name_check()
    if mod == 1: creating_export_file(lst, name_new_file, '\n')
    else: creating_export_file(lst, name_new_file, '***')


# производит запись в соответствии с выбранным режимом
def creating_export_file(lst, name, mod):
    if mod == '\n':
        with open(f'{name}.txt', 'w', encoding="utf-8") as page:
            for i in lst:
                page.write(i)
        view.progress_export(name + '.txt')
    else:
        count = 0
        with open(f'{name}.txt', 'w', encoding="utf-8") as page:
            for i in lst:
                if '\n' in i and i != '\n' and count != 3:
                    page.write(i[:len(i)-1] + mod)
                    count += 1
                elif '\n' in i and i != '\n' and count == 3:
                    page.write(i[:len(i)-1])
                    count = 0
                else: page.write('\n')
        view.progress_export(name + '.txt')