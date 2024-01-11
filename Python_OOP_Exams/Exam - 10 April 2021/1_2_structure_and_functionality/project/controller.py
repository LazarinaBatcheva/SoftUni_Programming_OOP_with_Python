from typing import Any, Optional

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    VALID_AQUARIUMS_TYPES = {"FreshwaterAquarium": FreshwaterAquarium,
                             "SaltwaterAquarium": SaltwaterAquarium}
    VALID_FISH_TYPES = {"FreshwaterFish": FreshwaterFish,
                        "SaltwaterFish": SaltwaterFish}
    VALID_DECORATION_TYPES = {"Ornament": Ornament,
                              "Plant": Plant}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: list[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type not in self.VALID_AQUARIUMS_TYPES:
            return "Invalid aquarium type."

        new_aquarium = self.VALID_AQUARIUMS_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type not in self.VALID_DECORATION_TYPES:
            return "Invalid decoration type."

        decoration = self.VALID_DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str) -> Optional[str]:
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_obj(aquarium_name, "name", self.aquariums)

        if aquarium is None:
            return

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str,
                 fish_species: str, price: float) -> Optional[str]:
        if fish_type not in self.VALID_FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_obj(aquarium_name, "name", self.aquariums)

        if aquarium is None:
            return

        fish = self.VALID_FISH_TYPES[fish_type](fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str) -> Optional[str]:
        aquarium = self.__find_obj(aquarium_name, "name", self.aquariums)

        if aquarium is None:
            return

        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str) -> Optional[str]:
        aquarium = self.__find_obj(aquarium_name, "name", self.aquariums)

        if aquarium is None:
            return

        value = sum([f.price for f in aquarium.fish]) + sum([d.price for d in aquarium.decorations])

        return f"The value of Aquarium {aquarium.name} is {value:.2f}."

    def report(self) -> str:
        return "\n".join([str(aq) for aq in self.aquariums])

    # HELPERS
    @staticmethod
    def __find_obj(searching_el, searching_attr: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attr) == searching_el), None)
