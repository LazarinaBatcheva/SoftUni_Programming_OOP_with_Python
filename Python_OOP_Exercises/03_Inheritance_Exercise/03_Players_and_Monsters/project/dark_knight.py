from project.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return super().__str__()
