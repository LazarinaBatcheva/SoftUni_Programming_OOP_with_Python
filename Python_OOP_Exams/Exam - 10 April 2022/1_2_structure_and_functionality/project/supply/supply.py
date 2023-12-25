from abc import ABC, abstractmethod


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = name

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, energy):
        if energy < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__energy = energy

    @property
    @abstractmethod
    def get_supply_type(self):
        pass

    def details(self) -> str:
        supply_type = self.get_supply_type

        return f"{supply_type}: {self.name}, {self.energy}"
