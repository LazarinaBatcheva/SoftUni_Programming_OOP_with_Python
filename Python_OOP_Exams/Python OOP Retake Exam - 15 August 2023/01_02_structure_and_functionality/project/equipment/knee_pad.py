from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15)

    @property
    def percent_increase(self) -> int:
        # Return a fixed value of 20, representing the percent increase for an KneePad.
        return 20
