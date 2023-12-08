from project.jockey import Jockey


class HorseRace:
    VALID_RACES_TYPES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: list[Jockey] = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, race_type):
        if race_type not in self.VALID_RACES_TYPES:
            raise ValueError("Race type does not exist!")
        self.__race_type = race_type
