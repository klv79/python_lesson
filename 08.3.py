class StrError(Exception):
    pass

my_list = []

while True:
    try:
        el = input('Введите елемент списка: ')
        if el == 'q':
            break
        if not el.isdigit():
            raise StrError(el)
        my_list.append(int(el))
    except StrError as err:
        print('Введите число!', err)
print(my_list)



