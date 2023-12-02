from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=1_000.0)

    @property
    def increase_advantage(self) -> int:
        # Return a fixed value of 115, representing the advantage increase for an OutdoorTeam.
        return 115
