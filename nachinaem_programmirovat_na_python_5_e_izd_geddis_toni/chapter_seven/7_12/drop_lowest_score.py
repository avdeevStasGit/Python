# Эта программа получает серию оценок за лабораторные работы и вычисляет среднюю оценку,
# отбрасывая самую низкую.


from get_scores import get_scores
from get_total import get_total


def main():
    # Получить от пользователя оценки.
    scores = get_scores()

    # Получить сумму оценок.
    total = get_total(scores)

    # Получить самую низкую оценку и вычесть.
    lowest = min(scores)

    total -= lowest

    # Вычислить среднее значение.
    average = total / (len(scores) - 1)

    # Показать среднее значение.
    print(f'Средняя оценка с учетом отброшенной самой низкой оценки: {average}')

if __name__ == '__main__':
    main()