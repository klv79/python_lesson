
my_list1 = [int(i) for i in input().split()]

print(my_list1)

my_list2 = [k for i, k in zip(my_list1, my_list1[1:]) if k > i]
print(my_list2)