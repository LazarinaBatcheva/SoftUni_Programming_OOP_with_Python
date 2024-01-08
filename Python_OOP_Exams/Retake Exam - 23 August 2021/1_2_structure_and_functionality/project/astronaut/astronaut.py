from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self. oxygen = oxygen
        self.backpack: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = name

    @property
    @abstractmethod
    def get_oxygen_decrease_value(self):
        pass

    def breathe(self):
        self.oxygen -= self.get_oxygen_decrease_value

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Oxygen: {self.oxygen}\n"
                f"Backpack items: {', '.join(self.backpack) if self.backpack else 'none'}")
