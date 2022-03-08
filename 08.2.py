class DelError(Exception):
    def __init__(self, namber_2):
        self.namber_2 = namber_2

try:
    namber_1 = int(input("Введите делимое: "))
    namber_2 = int(input("Введите делитель: "))
    if namber_2 == 0:
        raise DelError("Ошибка деления на 0")
except ValueError:
    print("Вы ввели не число")
except DelError as err:
    print(err)
else:
    print(f"Результат деления: {namber_1 / namber_2}")

