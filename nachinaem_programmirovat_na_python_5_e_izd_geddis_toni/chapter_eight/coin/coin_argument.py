# Эта программа передает объект Coin
# в качестве аргумента в функцию.
import coin

# Главная функция
def main():
    # Создать объект Coin
    my_coin = coin.Coin()

    # Эта функция покажет Орел.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    flip(my_coin)

    # Орел либо решка может показать.
    print(my_coin.get_sideup())

# Функция flip подбрасывает монету.
def flip(coin_obj):
    coin_obj.toss()

if __name__ == '__main__':
    main()