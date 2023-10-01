from car import Car
from racecar import RaceCar

car = Car(
    name="Test",
    price=8_900_900,
    volume=0,
    max_volume=120,
    max_speed=300
)

print(car.max_speed)
print(car.max_volume)
print(car)


racecar = RaceCar(
    name="Test",
    price=8_900_900,
    volume=0,
    max_volume=120,
    max_speed=300,
    team="Ferrari"
)

for fuel in range(10):
    racecar.refueling(fuel)

print(*racecar.last_10_refuels(), sep="\n")