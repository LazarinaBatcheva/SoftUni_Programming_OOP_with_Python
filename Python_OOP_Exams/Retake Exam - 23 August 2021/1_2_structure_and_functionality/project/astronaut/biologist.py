from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 70)

    @property
    def get_oxygen_decrease_value(self) -> int:
        return 5
