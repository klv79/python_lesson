revenue = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
profit = revenue - costs

if profit > 0:
    print("Прибыль = ", profit)
    rent = profit / revenue * 100
    print(F"Рентабельность {rent:.2f}%")
    number = int(input("Численность сотрудников: "))
    print(f"Выручка на одного сотрудника составила: {profit / number:.2f}")
elif profit < 0:
    print("Убытки составили: ", profit)
else:
    print("Прибыль равна 0")

