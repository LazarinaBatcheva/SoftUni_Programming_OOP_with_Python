from typing import Any

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: list[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Any:
        return next((astronaut for astronaut in self.astronauts if astronaut.name == name), None)
