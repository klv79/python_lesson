with open("my_f5.txt", "w", encoding="utf-8") as my_f5:
    print('Введите числа через пробел ')
    my_list1 = [int(i) for i in input().split()]
    for el in my_list1:
        el = str(el)
        my_f5.write(el)
        my_f5.write(" ")
    print(f'\nСумма чисел равна {sum(my_list1)} ', file=my_f5)

