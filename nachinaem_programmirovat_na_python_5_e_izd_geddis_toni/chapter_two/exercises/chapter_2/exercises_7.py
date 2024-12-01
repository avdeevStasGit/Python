# Расход бензина в расчете на километры пройденного пути.

# Расход бензина в расчете на километры пройденного автомобилем
# пути можно вычислить на основе формулы:
# расход = пройденные километры / расход бензина в литрах.
# Напишите программу, которая запрашивает у пользователя число
# пройденных километров и расход бензина в литрах. Она должна
# рассчитать расход бензина автомобилем
# и показать результат.

# пройденные километры.
kilometersTraveled = 0.0
# Пройденные километры.
gasolineConsumption = 0.0

driverKilometers = float(input('Введите число пройденых километров: '))
driverPetrol = float(input('Введите расход бензина в литрах: '))

kilometersTraveled = kilometersTraveled + driverKilometers
gasolineConsumption = gasolineConsumption + driverPetrol

# рассчитаываеем расход бензина автомобилем.
expenditure = kilometersTraveled / gasolineConsumption

print(f'Расход бензина автомобилем: {expenditure:,.2f} км\литр.')