from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    STARTING_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, 120)

    @property
    def get_oxygen_reduce_value(self) -> float:
        return 0.6

    @property
    def get_starting_oxygen_level(self) -> int:
        return self.STARTING_OXYGEN_LEVEL

