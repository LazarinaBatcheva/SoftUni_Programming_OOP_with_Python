from abc import ABC, abstractmethod
from typing import List

from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[BaseRobot] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def get_service_type(self):
        pass

    def details(self) -> str:
        robot_names = " ".join(r.name for r in self.robots) if self.robots else "none"

        return (f"{self.name} {self.get_service_type}:\n"
                f"Robots: {robot_names}")

