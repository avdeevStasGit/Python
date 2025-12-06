# Эта программа консервирует объекты CellPhone.
import pickle
import cellphone

# Константа для имени файла.
FILENAME = 'cellphones.dat'

def main():
    again = 'д'

    output_file = open(FILENAME, 'wb')

    while again.lower() == 'д':
        # Получить данные о сотовом телефоне.
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))


        phone = cellphone.CellPhone(man, mod, retail)

        # Законсервировать объект и записать его в файл.
        pickle.dump(phone, output_file)

        again = input('Введете еще один элемент данных? (д\н):')

        output_file.close()
        print(f'Данные записаны в {FILENAME}')

if __name__ == '__main__':
    main()