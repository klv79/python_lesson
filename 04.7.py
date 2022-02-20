from math import factorial

def fact1(n):
    yield factorial(n)

n = int(input("Фкториал какого числа нужно вычислить? "))
for el in fact1(n):
    print(el)

def fact2(n):
    k = 1
    for i in range(k, n+1):
        k = k * i
        yield k

for l in fact2(n):
    print(l)