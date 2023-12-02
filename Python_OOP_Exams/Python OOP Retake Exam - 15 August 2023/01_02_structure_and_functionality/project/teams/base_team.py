from abc import ABC, abstractmethod
from math import floor
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    @abstractmethod
    def increase_advantage(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")

        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    def find_total_price_of_team_equipment(self) -> int:
        # Returns the total price of the team's equipment.
        return sum(eq.price for eq in self.equipment)

    def find_avg_team_protection(self) -> float:
        # Returns the average protection value of the team's equipment.
        return sum(eq.protection for eq in self.equipment) / len(self.equipment) if self.equipment else 0

    def win(self):
        # Increases the team's advantage and increments the win count.
        self.advantage += self.increase_advantage
        self.wins += 1

    def calculate_score(self):
        # Calculates and returns the team's score
        return self.advantage + sum(eq.protection for eq in self.equipment)

    def get_statistics(self) -> str:

        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {self.find_total_price_of_team_equipment():.2f}\n"
                f"Average Protection: {floor(self.find_avg_team_protection())}")
