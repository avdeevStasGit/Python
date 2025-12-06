# Класс Contact содержит контактную информацию.


class Contact:
    # Метод init инициализирует атрибуты.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # Метод set_name устанавливает атрибут name.
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def __str__(self):
        return f'Имя: {self.__name}\n' + \
                f'Телефон: {self.__phone}\n' + \
                f'Электронная почта: {self.__email}'