# Чаевые, налог и общая сумма.
# Напишите программу, которая вычисляет общую стоимость
# заказанных блюд в ресторане.
# Программа должна попросить пользователя ввести
# стоимость еды, вычислить размер 18-процентных чаевых и
# 7-процентного налога с продаж и показать все стоимости и итоговую сумму.

# Стоимость еды.
food = 0.0

# Чаевые.
tips = 0.18

# Налог.
TAX = 0.07

# Просим пользователя ввести стоимость блюд заказанных в ресторане.
priceDishes = float(input('Введите общюю стоимость блюд заказанных' +
                    ' в ресторане: '))

# Передаем значение общей стоимости еды в food.
food = priceDishes

# Размер 18-процентных чаевых.
totalTips = food * tips

# Налог с продаж.
totalTax = priceDishes * TAX

totalSum = food + totalTips + totalTax

print(f'Cтоимость блюд заказанных в ресторане: {food} \n'
      f'Чаевые: ${totalTips:.2f} \n'
      f'Налог: ${totalTax:.2f} \n'
      f'Итоговая сумма: ${totalSum:.2f}')