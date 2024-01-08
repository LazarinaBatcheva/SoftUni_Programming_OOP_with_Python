from typing import Any, Optional

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    VALID_DRINK_TYPES = {"Tea": Tea, "Water": Water}
    VALID_TABLES_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: list[BakedFood] = []
        self.drinks_menu: list[Drink] = []
        self.tables_repository: list[Table] = []
        self.total_income: float = 0.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = name

    def add_food(self, food_type: str, name: str, price: float) -> Optional[str]:
        # Check for valid food type
        if food_type not in self.VALID_FOOD_TYPES:
            return

        food = self.find_obj(name, "name", self.food_menu)

        if food is not None:
            raise Exception(f"{food_type} {name} is already in the menu!")

        # Create new food object and add it in menu
        new_food = self.VALID_FOOD_TYPES[food_type](name, price)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> Optional[str]:
        # Check for valid drink type
        if drink_type not in self.VALID_DRINK_TYPES:
            return

        drink = self.find_obj(name, "name", self.drinks_menu)

        if drink is not None:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        # Create new drink object and add it in menu
        new_drink = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> Optional[str]:
        # Check for valid table type
        if table_type not in self.VALID_TABLES_TYPES:
            return

        table = self.find_obj(table_number, "table_number", self.tables_repository)

        if table is not None:
            raise Exception(f"Table {table_number} is already in the bakery!")

        # Create new drink object and add it in menu
        new_table = self.VALID_TABLES_TYPES[table_type](table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str) -> str:
        table = self.find_obj(table_number, "table_number", self.tables_repository)

        if table is None:
            return f"Could not find table {table_number}"

        missing_food = list(food_names)

        for f_name in food_names:
            for food in self.food_menu:
                if f_name == food.name:
                    table.order_food(food)
                    missing_food.remove(f_name)

        order = [f"Table {table_number} ordered:"]
        order.extend(repr(food) for food in table.food_orders)
        order.append(f"{self.name} does not have in the menu:")
        order.append("\n".join(missing_food))

        return "\n".join(order)

    def order_drink(self, table_number: int, *drinks_names: str) -> str:
        table = self.find_obj(table_number, "table_number", self.tables_repository)

        if table is None:
            return f"Could not find table {table_number}"

        missing_drinks = list(drinks_names)

        for d_name in drinks_names:
            for drink in self.drinks_menu:
                if d_name == drink.name:
                    table.order_drink(drink)
                    missing_drinks.remove(d_name)

        order = [f"Table {table_number} ordered:"]
        order.extend(repr(drink) for drink in table.drink_orders)
        order.append(f"{self.name} does not have in the menu:")
        order.append("\n".join(missing_drinks))

        return "\n".join(order)

    def leave_table(self, table_number: int) -> str:
        table = self.find_obj(table_number, "table_number", self.tables_repository)

        if table is not None:
            table_bill = table.get_bill()
            self.total_income += table_bill
            table.clear()
            return (f"Table: {table_number}\n"
                    f"Bill: {table_bill:.2f}")

    def get_free_tables_info(self) -> str:
        free_tables = [t.free_table_info() for t in self.tables_repository if t.free_table_info() is not None]

        return "\n".join(free_tables)

    def get_total_income(self) -> str:
        return f"Total income: {self.total_income:.2f}lv"

    # HELPERS
    @staticmethod
    def find_obj(searching_el, searching_attr: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attr) == searching_el), None)
