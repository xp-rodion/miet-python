from datetime import datetime
from car import Car


class RaceCar(Car):

    def __init__(self, name: str, price: float, volume: float, max_speed: int, max_volume: float, team: str):
        super().__init__(name, price, volume, max_speed, max_volume)
        self.team = team
        self.refuels = []

    def refueling(self, fuel: float) -> None:
        if self.max_volume < fuel + self.volume:
            raise ValueError("Бак переполнен")
        self.volume += fuel
        log_refuel = self.create_log_refuel(fuel, self.volume)
        self.refuels.append(log_refuel)

    @staticmethod
    def create_log_refuel(fuel: float, now_volume: float) -> str:
        return f"Заправлено: {fuel}; Текущий объем бензобака: {now_volume}; Время заправки {datetime.now()}"

    def last_10_refuels(self):
        if len(self.refuels) < 10:
            raise ValueError("Кол-во заправок меньше 10")
        return self.refuels[-10:]

    def __lt__(self, other):
        if not isinstance(other, RaceCar):
            raise TypeError("Объект не того типа данных")
        return self.max_speed < other.max_speed
