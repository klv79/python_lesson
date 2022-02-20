from collections import Counter
my_list1 = [int(i) for i in input().split()]

my_list2 = dict(Counter(my_list1))
print(my_list2)

my_list3 = [x for x, y in my_list2.items() if y==1]
print(my_list3)

