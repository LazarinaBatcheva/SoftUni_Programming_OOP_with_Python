import re

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list[Meal] = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        pattern = r"^0\d{9}$"
        if not re.match(pattern, phone_number):
            raise ValueError("Invalid phone number!")
        self.__phone_number = phone_number
