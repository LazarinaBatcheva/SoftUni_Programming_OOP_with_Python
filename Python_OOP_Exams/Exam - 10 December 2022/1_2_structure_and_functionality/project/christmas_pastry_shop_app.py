from typing import Any

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_VALID_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_VALID_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0.0

    @staticmethod
    def find_object(looking_name, name_attribute: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, name_attribute) == looking_name), None)

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:
        if type_delicacy not in self.DELICACY_VALID_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.find_object(name, "name", self.delicacies)

        if delicacy is not None:
            raise Exception(f"{name} already exists!")

        new_delicacy = self.DELICACY_VALID_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:
        if type_booth not in self.BOOTH_VALID_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.find_object(booth_number, "booth_number", self.booths)

        if booth is not None:
            raise Exception(f"Booth number {booth_number} already exists!")

        new_booth = self.BOOTH_VALID_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        for booth in self.booths:
            if not booth.is_reserved:
                if booth.capacity >= number_of_people:
                    booth.reserve(number_of_people)
                    return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str:
        booth = self.find_object(booth_number, "booth_number", self.booths)

        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.find_object(delicacy_name, "name", self.delicacies)

        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int) -> str:
        booth = self.find_object(booth_number, "booth_number", self.booths)

        price_of_all_orders = sum(delicacy.price for delicacy in booth.delicacy_orders)
        total_bill = booth.price_for_reservation + price_of_all_orders

        self.income += total_bill

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."

    def get_income(self) -> str:
        return f"Income: {self.income:.2f}lv."
