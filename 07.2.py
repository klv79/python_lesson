from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, razmer):
        self.razmer = razmer

    @property
    def use(self):
        return f'Необходимо  {self.razmer / 6.5 + 0.5 + 2 * self.razmer + 0.3 :.2f} метров ткани'

    @abstractmethod
    def abs(self):
        return 'не то'


class Coat(Clothes):
    def use(self):
        return f'Для пошива пальто нужно: {self.razmer / 6.5 + 0.5 :.2f} ткани'

    def abs(self):
        return 'Опять не то'


class Costume(Clothes):
    def use(self):
        return f'Для пошива костюма нужно: {2 * self.razmer + 0.3 :.2f} ткани'

    def abs(self):
        return 'Снова не то'


coat = Coat(698)
costume = Costume(178)
print(coat.use())
print(costume.use())

