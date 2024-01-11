from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    @property
    def get_fish_type(self) -> str:
        return "FreshwaterFish"

    def eat(self):
        self.size += 3
