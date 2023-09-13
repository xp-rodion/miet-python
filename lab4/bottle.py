from item import Item


class Bottle(Item):

    def __init__(self, volume: float, price: float, height: float, width: float, length: float):
        self.volume = volume
        super().__init__(price, height, width, length)

    def __add__(self, other):
        if isinstance(other, Bottle):
            return self.volume + other.volume
        raise TypeError("Объект не того типа!")

    def __str__(self):
        return f"Объем: {self.volume} - Цена: {self.price}"
