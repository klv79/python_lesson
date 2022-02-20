from  itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)
i = 0
for l in cycle(["Word", False, 1985, "и т.д."]):
    if i > 10:
        break
    print(l)
    i += 1
