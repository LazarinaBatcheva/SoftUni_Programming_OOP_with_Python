import re
from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    # Maps for equipment and team types
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam,  "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def available_capacity(self) -> int:
        return self.capacity - len(self.teams)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r"^[A-Za-z0-9]+$"
        if not re.match(pattern, value):
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def find_equipment_for_sell(self, equipment_type):
        return next((eq for eq in reversed(self.equipment) if eq.__class__.__name__ == equipment_type), None)

    def find_team_by_name(self, team_name: str):
        return next((t for t in self.teams if t.name == team_name), None)

    @staticmethod
    def determine_winner(team1, team2) -> str:
        team1_score = team1.calculate_score()
        team2_score = team2.calculate_score()

        if team1_score == team2_score:
            return "No winner in this game."

        winner, loser = sorted((team1, team2), key=lambda team: -team.calculate_score())
        winner.win()

        return f"The winner is {winner.name}."

    def add_equipment(self, equipment_type: str) -> str:
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        equipment = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int) -> str:
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")
        if not self.available_capacity:
            return "Not enough tournament capacity."

        team = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    # Method to sell equipment to a team
    def sell_equipment(self, equipment_type: str, team_name: str) -> str:
        equipment_for_sell = self.find_equipment_for_sell(equipment_type)
        team = self.find_team_by_name(team_name)

        if team.budget < equipment_for_sell.price:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment_for_sell)
        team.budget -= equipment_for_sell.price
        self.equipment.remove(equipment_for_sell)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str) -> str:
        team = self.find_team_by_name(team_name)

        if team is None:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    # Method to increase the price of a specific type of equipment
    def increase_equipment_price(self, equipment_type: str) -> str:
        number_of_changed_equipment = 0
        for eq in self.equipment:
            if eq.__class__.__name__ == equipment_type:
                eq.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    # Method to play a game between two teams
    def play(self, team_name1: str, team_name2: str) -> str:
        team1 = self.find_team_by_name(team_name1)
        team2 = self.find_team_by_name(team_name2)

        if type(team1) is not type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        return self.determine_winner(team1, team2)

    # Method to get tournament statistics
    def get_statistics(self) -> str:
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"]

        sorted_teams = sorted(self.teams, key=lambda team: -team.wins)
        result.extend(team.get_statistics() for team in sorted_teams)

        return "\n".join(result)
