from book import Book
from bottle import Bottle


bottle1 = Bottle(
    volume=1.5,
    price=300,
    height=210,
    width=200,
    length=300,
)

bottle2 = Bottle(
    volume=1,
    price=500,
    height=105,
    width=100,
    length=200,
)

assert bottle1 + bottle2 == 2.5
print(bottle1)

book = Book(
    name="Idiot",
    price=1000,
    height=125,
    width=150,
    length=300,
)

price_after_sale = book.computed_price_with_sale(25)
assert price_after_sale == 750

print(book.count_items_in_box(1000, 1200, 2000))
