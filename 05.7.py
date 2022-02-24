import json
my_f7 = open("text_7.txt", "r", encoding="utf-8")
for i in my_f7:
    print(i, end="")
my_f7.seek(0)
List = my_f7.read().split("\n")[:-1]
dict = dict()
for i in List:
    key = i.split(" ")[0]
    value = i.split(" ")[1:]
    dict[key] = value

dict_prib = {}
dict_ub = {}
dict_srprib = {}

for key in dict:
    dict.get(key).pop(0)
    str = [int(x) for x in dict.get(key)]
    if (str[0]-str[1]) >= 0:
        print(f'Фирма с прибылью {key} , {str[0] - str[1]}')
        dict_prib[key] = str[0] - str[1]
    else:
        print(f'Фирма с убытком {key} , {str[0] - str[1]}')
        dict_ub[key] = str[0] - str[1]
dict_srprib["Sred_prib"] = sum(dict_prib.values()) / len(dict_prib)
Result_spisok = [dict_prib, dict_srprib, dict_ub]
print(Result_spisok)

j_result = json.dumps(Result_spisok)
with open("text_71.txt", "w", encoding='utf-8') as f:
    json.dump(Result_spisok, f)




my_f7.close()