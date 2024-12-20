# Налог с продаж.
# Напишите программу, которая попросит
# пользователя ввести величину покупки. Затем программа
# должна вычислить федеральный и региональный налоги с продаж.
# Допустим, что федеральный налог с продаж составляет 5%,
# а региональный — 2.5%. Программа должна показать сумму покупки,
# федеральный налог с продаж, региональный налог с продаж, общий
# налог с продаж и общую сумму продажи (т. е. сумму покупки и общего
# налога с продаж).
# Подсказка', для представления 2.5% используйте значение 0.025,
# для представления 5% — 0.05.

# Федеральный налог.
FEDERAL_TAX = 0.05

# Региональный налог.
REGIONAL_TAX = 0.025

# Величина покупки пользователя.
purchaseAmount = float(input('Введите величину покупки: '))

federalTax =  purchaseAmount * FEDERAL_TAX

regionalTax = purchaseAmount * REGIONAL_TAX

generalTax = federalTax + regionalTax

totalSale = purchaseAmount + generalTax

print(f'Сумма покупки: {purchaseAmount} \n'
      f'Федеральный налог с продаж: {federalTax} \n'
      f'Региональный налог с продаж: {regionalTax} \n'
      f'Общий налог с продаж: {generalTax} \n'
      f'Сумма покупки и общего налога с продаж: {totalSale}')