# Функция change изменяет существующую
# запись в словаре birthdays.
def change(birthdays):
    #Получить искомое имя.
    name = input('Введите имя: ')

    if name in birthdays:
        # Получить новый день рождения.
        bday = input('Введите новый день рождения: ')

        # Обновить запись.
        birthdays[name] = bday
    else:
        print('Это имя не найдено.')

