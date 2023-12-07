from abc import ABC, abstractmethod

from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: list[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = capacity

    @property
    @abstractmethod
    def getting_price_per_person_for_a_booth(self):
        pass

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.getting_price_per_person_for_a_booth
        self.is_reserved = True
