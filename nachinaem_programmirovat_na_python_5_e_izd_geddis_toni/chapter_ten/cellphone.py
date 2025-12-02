# Класс CellPhone содержит данные о сотовом телефоне.

class CellPhone:
    # Метод __init__ инициализирует атрибуты.
    def __init__(self, manufact, model, price):
        self.manufact = manufact
        self.__model = model
        self.__retail_price = price

    # Метод set_manufact принимает аргумент для
    # производителя телефона.
    def set_manufact(self, manufact):
        self.__manufact = manufact

    # Метод set_model принимает аргумент для
    # номера модели телефона.

    def set_model(self, model):
        self.__model = model

    # Метод set_retail_price принимает аргумент для
    # розничной ценф телефона.

    def set_retail_price(self, price):
        self.__retail_price = price



    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

