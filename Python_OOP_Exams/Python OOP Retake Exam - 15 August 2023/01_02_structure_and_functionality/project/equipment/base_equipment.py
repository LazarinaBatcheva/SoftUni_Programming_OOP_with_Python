from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @property
    def protection(self):
        return self.__protection

    @protection.setter
    def protection(self, value):
        if value < 0:
            raise ValueError("Protection cannot be negative.")

        self.__protection = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Protection cannot be negative.")

        self.__price = value

    # take percent increase for each equipment price
    @property
    @abstractmethod
    def percent_increase(self):
        pass

    def increase_price(self):
        self.price *= (1 + self.percent_increase / 100)
        return self.price
