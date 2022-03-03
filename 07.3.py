class Kletka:
    def __init__(self, perem):
        self.perem = int(perem)

    def __add__(self, other):
        return f'{self.perem + other.perem}'

    def __sub__(self, other):
        sub = self.perem - other.perem
        return sub
    def __truediv__(self, other):
        return self.perem // other.perem

    def __mul__(self, other):
        return self.perem * other.perem

    def make(self, row):
        result = ''
        for i in range(int(self.perem / row)):
            result += '*' * row + '\n'
        result += '*' * (self.perem % row) + '\n'
        return result


kl1 = Kletka(25)
kl2 = Kletka(4)
print(kl1 + kl2)
print(kl1 - kl2)
print(kl1 / kl2)
print(kl1 * kl2)
print(kl1.make(11))