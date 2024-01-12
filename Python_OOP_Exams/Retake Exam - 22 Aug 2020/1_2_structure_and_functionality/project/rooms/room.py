from abc import ABC, abstractmethod

from project.people.child import Child


class Room(ABC):
    room_cost = None

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: list[Child] = []
        self.appliances: list = []
        self.expenses: float = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, expenses):
        if expenses < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = expenses

    def calculate_expenses(self, *args):
        total_expenses = 0
        for arg in args:
            for item in arg:
                total_expenses += item.get_monthly_expense()
        self.expenses = total_expenses

    def __str__(self):
        result = [f"{self.family_name} with {self.members_count} members. "
                  f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]

        if self.children:
            for i, child in enumerate(self.children):
                result.append(f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$")

        if self.appliances:
            result.append(f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$")

        return "\n".join(result)
