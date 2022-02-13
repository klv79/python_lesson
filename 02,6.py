n = int(input('Введите количество наименований товаров: '))
resalt = []
i = 1
while i <= n:
    slovar = {}
    korteg = ()
    spisok = []
    key1 = input('Введите наименование товара: ')
    slovar['наименование'] = key1
    key2 = input('Введите стоимость товара: ')
    slovar['стоимость'] = key2
    key3 = input('Введите количество товара: ')
    slovar['количество'] = key3
    key3 = input('Введите единицу товара: ')
    slovar['ед'] = key3
    spisok.append(i)
    spisok.append(slovar)
    korteg = tuple(spisok)
    resalt.append(korteg)
    i+=1
print(resalt)








