from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name.strip()) < 4:
            raise ValueError(f"Horse name {name} is less than 4 symbols!")
        self.__name = name

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if speed > self.get_max_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = speed

    @property
    @abstractmethod
    def get_max_speed(self):
        pass

    @property
    @abstractmethod
    def get_speed_increase_value(self):
        pass

    def train(self) -> None:
        max_speed = self.get_max_speed
        speed_increase = self.get_speed_increase_value

        self.speed = min(self.speed + speed_increase, max_speed)
