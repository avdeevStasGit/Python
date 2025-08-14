# Эта программа демонстрирует лексемизацию строковых литералов.

def main():
    str1 = 'one two tree four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    display_tokens(str1, ' ')
    display_tokens(str2, ':')
    display_tokens(str3, '/')

# Функция display_tokens выводит на экран лексемы,
# находящиеся в строковом литерале. Параметр data
# является строковым литералом, подлежащим ленксемизации,
# а параметр delimiter - разделителем.
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Лексема: {item}')

if __name__ == '__main__':
    main()