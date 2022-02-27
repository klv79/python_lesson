class Car:
    def __init__(self, s, c, n, i):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = bool(i)

    def go(self):
        print(f'Car {self.name} start!')

    def stop(self):
        print(f'Car {self.name} stop!')

    def turn(self, vector):
        print(f'Car {self.name} go {vector}!')

    def show_speed(self):
        print(f'Go car {self.name} with {self.speed}!')

class TownCar(Car):
    def f_litr(self, litr):
        print(f'Car {self.name} use {litr}l on 100km!')

class SportCar(Car):
    def f_power(self, power):
        print(f'Car {self.name} power {power}l.s!')
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Go car {self.name} with {self.speed} speed exceeding!')
        else:
            print(f'Go car {self.name} with {self.speed} !')
class WorkCar(Car):
    def kol_vo(self, kol):
        print(f'Автомобиль {self.name} с количеством пассажиров {kol}!')
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Go car {self.name} with {self.speed} speed exceeding!')
        else:
            print(f'Go car {self.name} with {self.speed} !')

class PoliceCar(Car):
    def param(self, x):
        print(f'Автомобиль {self.name} с параметром {x}!')


auto_1 = Car('60', 'blue', 'Lada', False)
auto_1.go()
auto_1.stop()
auto_1.turn('left')
auto_1.show_speed()
print()
auto_2 = TownCar('40', 'white', 'Mazda Family', False)
auto_2.go()
auto_2.stop()
auto_2.turn('right')
auto_2.f_litr('6')
auto_2.show_speed()
print()
auto_3 = SportCar('180', 'red', 'Ferrari', False)
auto_3.go()
auto_3.stop()
auto_3.turn('forward')
auto_3.f_power('600')
auto_3.show_speed()
print()
auto_4 = WorkCar('60', 'blue', 'Газель', False)
auto_4.go()
auto_4.stop()
auto_4.turn('лево')
auto_4.show_speed()
auto_4.kol_vo('15')
print()
auto_5 = PoliceCar('100', 'white', 'Toyota', True)
auto_5.go()
auto_5.stop()
auto_5.turn('right')
auto_5.show_speed()
auto_5.param('"параметр"')
