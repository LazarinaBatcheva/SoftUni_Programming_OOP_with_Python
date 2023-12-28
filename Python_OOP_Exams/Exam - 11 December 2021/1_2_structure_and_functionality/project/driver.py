from typing import Optional

from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car: Optional[Car] = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = name
