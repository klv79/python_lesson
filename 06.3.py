class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position (Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname} ')
    def get_total_income(self):
        print(f'доход {self._income.get("wage")}, премия {self._income.get("bonus")}')


a = Position("Иван", "Иванов", "Аналитик", "4000$", "5000$")
a.get_full_name()
a.get_total_income()
