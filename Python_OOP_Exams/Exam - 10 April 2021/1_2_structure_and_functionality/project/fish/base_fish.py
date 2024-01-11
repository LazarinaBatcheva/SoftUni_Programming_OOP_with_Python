from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = name

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        if species.strip() == "":
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = species

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = price

    @property
    @abstractmethod
    def get_fish_type(self):
        pass

    @abstractmethod
    def eat(self):
        pass
