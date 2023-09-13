from item import Item


class Book(Item):
    def __init__(self, name: str, price: float, height: float, width: float, length: float):
        self.name = name
        super().__init__(price, height, width, length)

    def computed_price_with_sale(self, sale: float):
        """
        Переопределение метода для высчета цены со скидкой
        """
        price = super().computed_price_with_sale(sale)
        if sale == 20:
            print("Активация купона с портала торгов")
        return price

    def __str__(self):
        return f"Книга: {self.name} - Цена: {self.price}"