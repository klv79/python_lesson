my_f2 = open("my_f2.txt", "r", encoding="utf-8")
k = 0
for i in my_f2:
    print(i, end="")
    print(f" Количество слов в строке № {k + 1} ", len(i.split()))
    print(f" Количество букв в строке № {k + 1} ", len(i.replace(" ", "")) - 1)
    k +=1
print(f"В файле {k} строки")


my_f2.close()





