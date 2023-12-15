from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Fish name should be determined!")
        self.__name = name

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if points < 1 or points > 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__points = points

    @property
    @abstractmethod
    def get_fish_type(self):
        pass

    def fish_details(self) -> str:
        return (f"{self.__class__.__name__}: {self.name} "
                f"[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]")
