class Car:
    def __init__(self, name: str, price: float, volume: float, max_speed: int, max_volume: float):
        self.name = name
        self.price = price
        self.volume = volume
        self.__max_volume = max_volume
        self.__max_speed = max_speed

    def __str__(self):
        return f"Car: {self.name}; max_speed: {self.max_speed}"

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed: int):
        self.__max_speed = max_speed

    @property
    def max_volume(self):
        return self.__max_volume

    @max_volume.setter
    def max_volume(self, max_volume: float):
        self.__max_volume = max_volume