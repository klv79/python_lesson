import re
my_f6 = open("text_6.txt", "r", encoding="utf-8")
for i in my_f6:
    print(i, end="")
my_f6.seek(0)
List = my_f6.read().split("\n")[:-1]
dict = dict()
for i in List:
    key = i.split(":")[0]
    value = i.split(":")[1:]
    dict[key] = value
dict1 = {}
for key in dict:
    res = re.findall(r'\b(?<!\.)\d+(?!\.)\b', str(dict.get(key)))
    st = [int(x) for x in res]
    dict1[key] = sum(st)

print(dict1)







my_f6.close()