from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):  # The SaltwaterFish could only live in SaltwaterAquarium
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    @property
    def get_fish_type(self) -> str:
        return "SaltwaterFish"

    def eat(self):
        self.size += 2
