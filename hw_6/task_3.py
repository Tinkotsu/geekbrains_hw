class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


person = Position('Jason', 'Moo', 'Director', 500, 300)
print(person.position)
print(person.income)
print(person.get_full_name())
print(person.get_total_income())
