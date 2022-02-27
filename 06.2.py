class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w
        print(l, w)
        self.metod()

    def metod(self):
        print(f'Для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см, необходимо {self._length * self._width * 25 / 1000}т массы асфальта ')

d = Road(25, 50)

