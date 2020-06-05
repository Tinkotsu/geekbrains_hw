class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        new = Cell(self.amount + other.amount)
        return new

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            new = Cell(self.amount - other.amount)
            return new

    def __mul__(self, other):
        new = Cell(self.amount * other.amount)
        return new

    def __truediv__(self, other):
        if other.amount > 0:
            new = Cell(self.amount // other.amount)
            return new

    def make_order(self, n):
        if n > 0:
            res = ''
            rest = self.amount
            while rest > 0:
                if rest > n:
                    res += '*' * n + '\n'
                else:
                    res += '*' * rest
                rest -= n
            return res


cell1 = Cell(10)
cell2 = Cell(2)
new_cell = cell1 * cell2
print(new_cell.make_order(3))
