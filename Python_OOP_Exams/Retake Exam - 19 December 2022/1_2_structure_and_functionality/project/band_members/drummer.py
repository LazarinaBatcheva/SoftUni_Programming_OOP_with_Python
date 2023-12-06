from typing import List

from project.band_members.musician import Musician


class Drummer(Musician):
    available_skills = ["play the drums with drumsticks",
                        "play the drums with drum brushes",
                        "read sheet music"]

    @property
    def get_skills(self) -> List[str]:
        return self.available_skills
