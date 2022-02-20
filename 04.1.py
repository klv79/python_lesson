from sys import argv

name, production, stavka, prize = argv

def zp(nam1, nam2, nam3):
    return nam1 * nam2 + nam3

print(zp(int(production), int(stavka), int(prize)))
