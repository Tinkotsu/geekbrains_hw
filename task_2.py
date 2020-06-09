from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    @property
    def cloth(self):
        res = self.param / 6.5 + 0.5
        return res


class Suit(Clothes):
    @property
    def cloth(self):
        res = 2 * self.param / + 0.3
        return res


coat = Coat(15)
suit = Suit(1.8)
print(coat.cloth)
print(suit.cloth)
