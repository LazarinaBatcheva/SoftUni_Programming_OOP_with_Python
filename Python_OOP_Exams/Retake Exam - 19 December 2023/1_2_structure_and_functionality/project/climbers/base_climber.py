from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List[str] = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, strength):
        if strength <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = strength

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    @property
    @abstractmethod
    def strength_comparison_value(self):
        pass

    def can_climb(self) -> bool:
        return self.strength >= self.strength_comparison_value

    def rest(self) -> None:
        self.strength += 15

    def __str__(self):
        return (f"{self.__class__.__name__}: /// "
                f"Climber name: {self.name} * "
                f"Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {', '.join(sorted(self.conquered_peaks))} ///")
