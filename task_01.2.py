time = int(input("Введите время в секундах:"))
hour = int(time / 3600)
minute = int(time / 60 - hour * 60)
second = int(time - hour * 3600 - minute * 60)
print(f"{hour}:{minute}:{second}")

