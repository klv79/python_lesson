my_f4 = open("text_4.txt", "r", encoding="utf-8")
my_f4_1 = open("text_4_1.txt", "w", encoding="utf-8")
for i in my_f4:
    print(i, end="")
my_f4.seek(0)
onstring = my_f4.read().split("\n")[:-1]
dict = dict()
for i in onstring:
    key = i.split("-")[0]
    value = i.split("-")[1:]
    value1 = int(value[0])
    dict[key] = value1
print(onstring)
print(dict)
dict["Один"] = dict.pop("One ")
dict["Два"] = dict.pop("Two ")
dict["Три"] = dict.pop("Three ")
dict["Четыре"] = dict.pop("Four ")
for key, value in dict.items():
  my_f4_1.write(f'{key} -  {value}\n')



print(dict)


my_f4.close()
my_f4_1.close()