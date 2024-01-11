from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    allowed_fish_type = "FreshwaterFish"

    def __init__(self, name: str):
        super().__init__(name, 50)
