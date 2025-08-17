# Эта программа применяет словарь в качестве колоды.
import random

def main():
    # Создать колоду карт.
    deck = create_deck()

    # Получить количество карт для раздачи.
    num_cards = int(input('Сколько карт раздать? '))

    # Раздать карты.
    deal_cards(deck, num_cards)