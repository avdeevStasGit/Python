# Функция get_total принимает список в качестве
# аргумента и возвращает сумму значений
# в списке.

def get_total(value_list):
    # Создать переменную для применения в качестве накопителя.
    total = 0.0

    for num in value_list:
        total += num

        return total

if __name__ == '__main__':
    main()