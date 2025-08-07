# Вывод файла на экран.
def main():
    open_file = open('numbers.txt', 'r')

    file_contents = open_file.read()

    open_file.close()

    print(file_contents)

if __name__ == '__main__':
    main()