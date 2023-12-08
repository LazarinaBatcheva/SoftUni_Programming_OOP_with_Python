from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREASE_VALUE = 2

    # def __init__(self, name: str, speed: int):
    #     super().__init__(name, speed)

    @property
    def get_max_speed(self) -> int:
        return self.MAX_SPEED

    @property
    def get_speed_increase_value(self) -> int:
        return self.SPEED_INCREASE_VALUE
