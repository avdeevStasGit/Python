# Эта программа читает и показывает содержимое
# файла philosophers.txt.
def main():
    # Открыть файл с именем philosophes.
    infile = open('philosophers.txt', 'r')

    # Прочитать содержимое файла.
    file_contents = infile.read()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные
    # в оперативную память.
    print(file_contents)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()