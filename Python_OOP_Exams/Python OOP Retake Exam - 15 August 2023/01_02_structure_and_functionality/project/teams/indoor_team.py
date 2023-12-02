from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=500.0)

    @property
    def increase_advantage(self) -> int:
        # Return a fixed value of 145, representing the advantage increase for an IndoorTeam.
        return 145
