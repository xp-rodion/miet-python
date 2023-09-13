import math


class Item:
    def __init__(self, price: float, height: float, width: float, length: float):
        self.price = price
        self.height = height
        self.width = width
        self.length = length

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        raise TypeError("Объект не того типа!")

    def computed_price_with_sale(self, sale: float):
        if sale > 100:
            raise ValueError("Нарушение скидки")

        price = self.price * (1 - (sale / 100))

        if price < 0.01:
            raise ValueError("Нарушена мин. цена")

        return price

    def count_items_in_box(self, b_height: float, b_width: float, b_length: float):
        if self.length > b_length or self.width > b_width or self.height > b_height:
            return 0
        item_volume = self.length * self.width * self.height
        box_volume = b_length * b_width * b_height
        count_items = math.floor(box_volume / item_volume)
        return count_items
