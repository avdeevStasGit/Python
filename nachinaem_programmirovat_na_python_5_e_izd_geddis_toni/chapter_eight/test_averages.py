# Эта программа читает результаты контрольных работ из
# файла CSV и вычисляет средний балл для каждого ученика.

def main():
    # Оnкрыть файл.
    csv_file = open('test_scores.csv', 'r')

    # Прочитать строки файла в список.
    lines = csv_file.readlines()

    # Закрыть файл.
    csv_file.close()


    # Обработать строки.
    for line in lines:
        # Получить результаты контрольных работ в виде лексем.
        tokens = line.split(',')

        # Подсчитать общее количество баллов за контрольные работы.
        total = 0.0
        for token in tokens:
            total += float(token)

        # Вычислить средний балл результатов контрольных работ.
        averege = total / len(tokens)
        print(f'Средний балл: {averege}')

if __name__ == '__main__':
    main()
