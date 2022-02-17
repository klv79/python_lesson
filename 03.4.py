def my_f(x, y):
    i = 1
    z = x
    while i < abs(y):
        z = z * x
        i += 1
    return 1 / z
x1 = int(input('Введите действительное положительное число x '))
y1 = int(input('Введите целое отрицательное число y '))
if y1 > 0:
    print('Вы ввели не отрицательное число')
else:
    try:
        print('Решение с помощью функции ', round(my_f(x = x1, y = y1), 3))
        print('Решение с помощью "**"', round((x1 ** y1), 3))
    except ZeroDivisionError:
        print('Ошибка! Попытка деления на 0 ')
