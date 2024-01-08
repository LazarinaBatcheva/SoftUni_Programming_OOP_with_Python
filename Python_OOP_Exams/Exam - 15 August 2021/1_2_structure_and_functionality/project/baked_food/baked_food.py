from abc import ABC


class BakedFood(ABC):
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = price

    def __repr__(self) -> str:
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
