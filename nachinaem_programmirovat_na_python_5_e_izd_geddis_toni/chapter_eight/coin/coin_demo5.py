# Эта программа импортирует имитационный модуль.
# и создает три экземпляра.

import coin

def main():
    # Создать три оъекта класса Coin.
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Показать повернутую вверх сторону каждой монеты.
    print('Вот три монеты, у которых эти стороны обращены вверх:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    # Подбросить монету.
    print('Подбросить все три монеты...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Показать повернутую вверх сторону каждой монеты.
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

    if __name__ == '__main__':
        main()