def my_func(slovo):
    """ Функция меняет первую строчную букву слова на заглавную.
        при помощи ASCII-кода для символа

    :param slovo: изменяемое слово
    :return: на выходе измененная буква + оставшийся срез слова
    """
    slovo_smoll = slovo[0]
    slovo_big = chr(ord(slovo_smoll) - ord('a') + ord('A'))
    return slovo_big + slovo[1:]
Str = input('Введите строку ').split()
new_Str = []
for slovo in Str:
    new_Str.append(my_func(slovo))
print(my_func(slovo=input('Введите слово ')))
print(' '.join(new_Str))