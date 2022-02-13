stroka = input('Введите строку ')
print(stroka)
stroka1 = stroka.split()
print(stroka1)
k = 1
for i in stroka1:
    print(f" Слово № {k}:", i[0:10])
    k+=1