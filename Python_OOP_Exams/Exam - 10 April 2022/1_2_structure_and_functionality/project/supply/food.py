from project.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)

    @property
    def get_supply_type(self) -> str:
        return self.__class__.__name__
