from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    _appliances: list = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = YoungCoupleWithChildren.room_cost
        self.children: list[Child] = list(children)
        self.appliances: list = YoungCoupleWithChildren._appliances * self.members_count
        self.calculate_expenses(self.appliances, self.children)
