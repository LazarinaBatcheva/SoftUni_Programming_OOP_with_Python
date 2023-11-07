class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{self.username} of type {class_name} has level {self.level}"
