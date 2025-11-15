# Функция delete удаляет запись из словаря birthdays.
def delete(birthdays):
    # Получить искомое имя.
    name = input('Введите имя: ')

    # Если имя найдено, то удалить эту запись.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Это имя не найдено.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()