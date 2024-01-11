from abc import ABC

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    allowed_fish_type = None

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list[BaseDecoration] = []
        self.fish: list[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = name

    def calculate_comfort(self) -> int:
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: BaseFish) -> str:
        if self.capacity == len(self.fish):
            return "Not enough capacity."

        if fish.get_fish_type != self.allowed_fish_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.get_fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> None:
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = [f.name for f in self.fish]

        return (f"{self.name}:\n"
                f"Fish: {' '.join(fish_names) if fish_names else 'none'}\n"
                f"Decorations: {len(self.decorations)}\n"
                f"Comfort: {self.calculate_comfort()}")
