from typing import List

from project.band_members.musician import Musician


class Guitarist(Musician):
    available_skills = ["play metal",
                        "play rock",
                        "play jazz"]

    @property
    def get_skills(self) -> List[str]:
        return self.available_skills
