# Эта программа вычисляет отпускную цену
# розничного товара.

# DISCOUNT_PERCENTAGE используется в качестве
# глобальной константы для процента скидки.
DISCOUNT_PERCENTAGE = 0.20

# Главная функция.
def main():
    # Получить обычную цену товара.
    reg_price = get_regular_price()

    # Получить сумму скидки.
    discount_amount = discount(reg_price)

    # Рассчитать отпускную цену.
    sale_price = seling_price(reg_price, discount_amount)

    # Показать отпускную цену.
    print(f'Отпускная цена составляет ${sale_price:,.2f}')

# Функция get_regular_price предлагает пользователю
# ввести обычную цену товара и возвращает
# это значение.
def get_regular_price():
    price = float(input('Введите обычную цену товара: '))
    return price

# Функция discount принимает цену товара в качестве
# аргумента и возвращает сумму скидки,
# указанную в DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Рассчитать отпускную цену.
def seling_price(reg_price, discount_amount):
    return reg_price - discount_amount

# Вызвать главную функцию.
main()