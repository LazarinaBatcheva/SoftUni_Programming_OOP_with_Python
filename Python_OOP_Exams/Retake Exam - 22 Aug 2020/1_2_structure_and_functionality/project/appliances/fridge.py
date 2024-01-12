from project.appliances.appliance import Appliance


class Fridge(Appliance):
    cost = 1.2

    def __init__(self):
        super().__init__(Fridge.cost)
        