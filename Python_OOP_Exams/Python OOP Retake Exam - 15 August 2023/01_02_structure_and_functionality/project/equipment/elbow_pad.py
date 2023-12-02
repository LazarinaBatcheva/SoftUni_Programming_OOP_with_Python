from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25)

    @property
    def percent_increase(self) -> int:
        # Return a fixed value of 10, representing the percent increase for an ElbowPad.
        return 10
