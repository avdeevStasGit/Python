# Эта программа имитирует бросание кубиков.
import random

# Констатнты для минимального и максимального случайных чисел.
MIN = 1
MAX = 6

def main():
    # Создать переменную, которая управляет циклом.
    again = 'д'

    # Имитировать юросание кубиков.
    while again == 'д' or again == 'Д':
        print('Бросаем кубики...')
        print('Значение граней:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать еще один бросок кубиков?
        again = input('Бросить кубики еще раз? (д = да): ')

# Вызвать главную функцию.
main()