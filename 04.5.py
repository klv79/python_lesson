from functools import reduce
from operator import mul

my_list = [int(i) for i in range(100, 1001, 2) ]
print(my_list)

my_list2 = reduce(mul, my_list)
print(my_list2)
