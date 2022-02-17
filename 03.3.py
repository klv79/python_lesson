def my_f(num_1, num_2, num_3):
    my_l = [num_1, num_2, num_3]
    my_l.remove(min(my_l))
    return sum(my_l)
try:
    print('Сумма наибольших двух чисел равна = ', my_f(num_1=int(input('Введите число №1 ')), num_2=int(input('Введите число №2 ')),
               num_3=int(input('Введите число №2 '))))
except ValueError:
    print('Ошибка! Нужны цифры! ')
