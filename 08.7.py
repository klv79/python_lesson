class ComplexNumber:
    def __init__(self, a):
        self.a = complex(a)

    def __add__(self, other):
        print(f'Сумма:')
        return f'n = {self.a.real + other.a.real} + {self.a.imag + other.a.imag} * j'

    def __mul__(self, other):
        print(f'Произведение:')
        return f'n = {self.a.real * other.a.real - (self.a.imag * other.a.imag)} + {self.a.imag * other.a.real + self.a.real * other.a.imag} * j'

    def __str__(self):
        return f'n = {self.a.real} + {self.a.imag} * j'


n_1 = ComplexNumber(2+3j)
n_2 = ComplexNumber(5+4j)
print(n_1)
print(n_2)
print(n_1 + n_2)
print(n_1 * n_2)
