from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    allowed_fish_type = "SaltwaterFish"

    def __init__(self, name: str):
        super().__init__(name, 25)
