from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    STARTING_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, 540)

    @property
    def get_oxygen_reduce_value(self) -> float:
        return 0.3

    @property
    def get_starting_oxygen_level(self) -> int:
        return self.STARTING_OXYGEN_LEVEL
