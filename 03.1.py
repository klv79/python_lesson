def my_f(num1, num2):
    return num1 / num2
try:
    print(round(my_f((int(input('Введите число №1 '))), int(input('Введите число №2 '))), 5))
except ValueError:
    print('Ошибка! Нужны цифры! ')
except ZeroDivisionError:
    print('Ошибка! Попытка деления на 0 ')








