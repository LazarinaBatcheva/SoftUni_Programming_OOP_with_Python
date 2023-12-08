from copy import copy
from typing import Any

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}

    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []
        self._receipt_id_generator = self.receipt_id_generator()

    @staticmethod
    def find_obj(looking_obj, obj_attribute: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, obj_attribute) == looking_obj), None)

    @staticmethod
    def check_if_client_shopping_list(client):
        if not client.shopping_cart:
            raise Exception(f"There are no ordered meals!")
        return client

    @staticmethod
    def receipt_id_generator():
        r_id = 1
        while True:
            yield r_id
            r_id += 1

    def register_client(self, client_phone_number: str) -> str:
        client = self.find_obj(client_phone_number, "phone_number", self.clients_list)

        if client is not None:
            raise Exception("The client has already been registered!")

        # create new client
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:
        for meal in meals:
            if meal.__class__ in self.VALID_MEALS_TYPES.values():
                self.menu.append(meal)

    def show_menu(self) -> str:
        self.if_menu_ready()    # check for at least 5 meals

        # adding details for each menu (name, price)
        result = [m.details() for m in self.menu]

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities) -> str:
        # **meal_names_and_quantities = {"meal name": desired quantity for meal}

        self.if_menu_ready()

        client = self.find_obj(client_phone_number, "phone_number", self.clients_list)

        if client is None:
            self.register_client(client_phone_number)
            client = self.find_obj(client_phone_number, "phone_number", self.clients_list)

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.find_obj(meal_name, "name", self.menu)
            if meal is None:
                raise Exception(f"{meal_name} is not on the menu!")
            elif quantity > meal.quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.find_obj(meal_name, "name", self.menu)
            meal.quantity -= quantity
            c_meal = copy(meal)
            c_meal.quantity = quantity
            client.shopping_cart.append(c_meal)
            client.bill += meal.price * quantity

        meal_names = [m.name for m in client.shopping_cart]
        return (f"Client {client_phone_number} "
                f"successfully ordered {', '.join(meal_names)} "
                f"for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str) -> str:
        client = self.find_obj(client_phone_number, "phone_number", self.clients_list)

        self.check_if_client_shopping_list(client)

        # if shopping list is not empty order canceled
        for c_meal in client.shopping_cart:
            meal = self.find_obj(c_meal.name, "name", self.menu)
            meal.quantity += c_meal.quantity

        client.shopping_cart.clear()
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str:
        client = self.find_obj(client_phone_number, "phone_number", self.clients_list)

        self.check_if_client_shopping_list(client)

        # if shopping list is not empty order finished
        client.shopping_cart.clear()
        total_paid_money = client.bill
        client.bill = 0
        receipt_id = next(self._receipt_id_generator)

        return (f"Receipt #{receipt_id} "
                f"with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    # helpers
    def if_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")