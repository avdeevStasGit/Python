# Главная функция.

# Эта программа применяет словарь для хранения
# имен и дней рождения друзей.

# Глобальные константы для пунктов меню.
MENU = 0
LOOCK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Главная функция.
def main():
    # Создать пустой словарь.
    birthdays = {}

    # Инициализировать переменную для выбора пользователя.
    choice = 0

    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()

        # Обработать выбранный вариант действий.
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)