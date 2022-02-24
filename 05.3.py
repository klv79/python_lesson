my_f3 = open("text_3.txt", "r", encoding="utf-8")
for i in my_f3:
    print(i, end="")
my_f3.seek(0)

onstring = my_f3.read().split("\n")[:-1]
dict = dict()

for i in onstring:
    key = i.split(" ")[0]
    value = i.split(" ")[1:]
    value1 = float(value[0])
    dict[key] = value1

for key in dict:
    if dict[key] < 20000:
        print('Сотрудник у котрого зп менее 20 тыс. ', key)
sum = 0

for key in dict:
    sum += dict[key]

print('Средняя зп сотрудников ', round(sum / len(dict), 2))


my_f3.close()
