from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list[BaseFish] = []
        self._competition_points: float = 0.0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = name

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, oxygen_level):
        if oxygen_level < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = oxygen_level

    @property
    def competition_points(self):
        return round(self._competition_points, 1)

    @property
    @abstractmethod
    def get_oxygen_reduce_value(self):
        pass

    @property
    @abstractmethod
    def get_starting_oxygen_level(self):
        pass

    def miss(self, time_to_catch: int) -> None:
        reduce_value = self.get_oxygen_reduce_value
        reduction = round(time_to_catch * reduce_value)

        if (self.oxygen_level - reduction) <= 0:
            self.oxygen_level = 0
            self.has_health_issue = True
            return
        self.oxygen_level = self.oxygen_level - reduction

    def renew_oxy(self):
        self.oxygen_level = self.get_starting_oxygen_level

    def hit(self, fish: BaseFish) -> None:
        if self.oxygen_level < fish.time_to_catch:
            self.oxygen_level = 0
            self.has_health_issue = True
            return

        self.oxygen_level -= fish.time_to_catch
        if self.oxygen_level == 0:
            self.has_health_issue = True
        self.catch.append(fish)
        self._competition_points += fish.points
        self._competition_points = round(self._competition_points, 1)

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.__class__.__name__}: "
                f"[Name: {self.name}, "
                f"Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, "
                f"Points earned: {self._competition_points}]")
