# Функция отыскивает имя
# в словаре birthdays.

def look_up(birthdays):
    # Получить искомое имя
    name = input('Введите имя: ')

    # Отыскать его в словаре.
    print(birthdays.get(name, 'Не найдено.'))