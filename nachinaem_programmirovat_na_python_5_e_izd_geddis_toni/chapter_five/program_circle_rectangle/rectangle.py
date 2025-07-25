# Модуль rectangle содержть функции, которые выполняют
# вычисления, связанные с прямоугольниками.

# Функция area принимает ширину и длину прямоугольника.
# в качестве аргументов и возвращает площадь прямоугольника.
def area(width, length):
    return width * length

# Функция perimeter принимает ширину и длину прямоугольника
# в качестве аргументов и возвращает периметр
# прямоугольника.
def perimeter(width, length):
    return 2 * (width + length)