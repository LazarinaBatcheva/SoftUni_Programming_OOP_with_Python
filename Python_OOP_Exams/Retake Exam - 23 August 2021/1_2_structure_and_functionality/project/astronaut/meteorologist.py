from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 90)

    @property
    def get_oxygen_decrease_value(self) -> int:
        return 15
