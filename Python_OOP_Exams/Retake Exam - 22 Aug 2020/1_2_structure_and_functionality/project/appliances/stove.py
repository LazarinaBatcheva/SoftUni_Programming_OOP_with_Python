from project.appliances.appliance import Appliance


class Stove(Appliance):
    cost = 0.7

    def __init__(self):
        super().__init__(Stove.cost)
