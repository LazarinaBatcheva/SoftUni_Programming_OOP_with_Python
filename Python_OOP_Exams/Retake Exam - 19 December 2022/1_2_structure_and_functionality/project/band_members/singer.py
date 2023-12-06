from typing import List

from project.band_members.musician import Musician


class Singer(Musician):
    available_skills = ["sing high pitch notes",
                        "sing low pitch notes"]

    @property
    def get_skills(self) -> List[str]:
        return self.available_skills
