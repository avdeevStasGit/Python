# Эта программа демонстрирует приминение метода append
# для добавления значений в список.

def main():
    # Создать пустой список.
    name_list = []

    again = 'д'

    while again == 'д':
        name = input('Введите имя: ')

        name_list.append(name)

        print('Желаете добавить еще одно имя?')
        again = input('д = да, все остальное = нет: ')
        print()

    print('Вот имена, которые были введены.')

    for name in name_list:
        print(name)

if __name__ == '__main__':
    main()