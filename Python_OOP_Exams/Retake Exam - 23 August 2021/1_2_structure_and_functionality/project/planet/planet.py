class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items: list[str] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = name
