from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    def __init__(self, name: str, points: float):
        super().__init__(name, points, 90)

    @property
    def get_fish_type(self):
        return self.__class__.__name__
