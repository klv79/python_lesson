def my_f():
    my_l = [int(i) if i != 'q' else exit() for i in input().split() ]
    Sum = sum(my_l)
    return Sum
Sum_m = 0
while True:
    Sum_m = Sum_m + my_f()
    print(Sum_m)


