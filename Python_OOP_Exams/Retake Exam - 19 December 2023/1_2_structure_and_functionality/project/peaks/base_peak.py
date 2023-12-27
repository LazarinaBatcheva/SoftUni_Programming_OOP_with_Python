from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self.__name = name

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, elevation):
        if elevation < 1500:
            raise ValueError("Peak elevation cannot be below 1500m.")
        self.__elevation = elevation

    @abstractmethod
    def calculate_difficulty_level(self):
        pass

    @abstractmethod
    def get_recommended_gear(self):
        pass
