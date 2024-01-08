from abc import ABC


class Drink(ABC):
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = name

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, portion):
        if portion <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.__portion = portion

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand.strip() == "":
            raise ValueError("Brand cannot be empty string or white space!")
        self.__brand = brand

    def __repr__(self) -> str:
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
