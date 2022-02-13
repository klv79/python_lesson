number = int(input('Введите месяц в виде целого числа от 1 до 12: '))
while number < 1 or number > 12:
    number = int(input('Ведите от 1 до 12: '))
vrem = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето',
        7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
print('Время года (метод dict): ', vrem[number])

vrem1 = ('Зима', 'Весна', 'Лето', 'Осень')
if number > 8 and number < 12:
    print('Время года (метод list): ', vrem1[3])
if number > 2 and number < 6:
    print('Время года (метод list): ', vrem1[1])
if number > 6 and number < 9:
    print('Время года (метод list): ', vrem1[2])
if number == 12 or number == 1 or number == 2:
    print('Время года (метод list): ', vrem1[0])





#print(vrem)