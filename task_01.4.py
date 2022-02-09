number = int(input("Введите целое положительное число: "))
number_max = 0

while number != 0:
    number1 = number % 10
    number //= 10
    if number_max <= number1:
        number_max = number1


print("Наибольшая цифра в числе: ", number_max)

