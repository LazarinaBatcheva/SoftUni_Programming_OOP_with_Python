from project.booths.booth import Booth


class OpenBooth(Booth):
    # def __init__(self, booth_number: int,  capacity: int):
    #     super().__init__(booth_number, capacity)

    @property
    def getting_price_per_person_for_a_booth(self):
        return 2.50
