
n = int(input("Введите количество элементов списка: "))
l = 0
my_list = []

while l < n:
    el = input('Введите елемент списка: ')
    my_list.append(el)
    l+=1
print(my_list)

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)



