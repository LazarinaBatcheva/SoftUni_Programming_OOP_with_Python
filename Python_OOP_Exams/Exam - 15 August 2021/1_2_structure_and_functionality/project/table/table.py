from abc import ABC

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: list[BakedFood] = []
        self.drink_orders: list[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = capacity

    def reserve(self, number_of_people: int) -> None:
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        return sum(food.price for food in self.food_orders) + sum(drink.price for drink in self.drink_orders)

    def clear(self) -> None:
        self.food_orders.clear()
        self.drink_orders.clear()
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self) -> str:
        if not self.is_reserved:
            return (f"Table: {self.table_number}\n"
                    f"Type: {self.__class__.__name__}\n"
                    f"Capacity: {self.capacity}")
