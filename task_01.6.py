result_a = int(input("Введите результат пробежки в первый день: "))
result_b = int(input("Введите желаемы результат: "))
result = result_a
i = 1
while result // result_b != 1:
    print(f"{i} день {result:.2f}")
    result = result * 1.1
    i = i + 1
print(f"Желаемого результата не менее {result_b} км. спортсмен достиг на {i} - ой день")
