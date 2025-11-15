# Функция добавляет новую запись
# в словарь birthdays.

def add(birthdays):
    # Получить имя и день рождения.
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')

    # Если имя не существует, то его добавить.
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Эта запись уже существует.')
