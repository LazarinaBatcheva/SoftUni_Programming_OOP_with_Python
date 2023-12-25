class Player:
    __PLAYERS_NAMES = set()

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name not valid!")
        if name in self.__PLAYERS_NAMES:
            raise Exception(f"Name {name} is already used!")

        self.__PLAYERS_NAMES.add(name)
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = age

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina):
        if not 0 <= stamina <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = stamina

    @property
    def need_sustenance(self) -> bool:
        return self.stamina < 100

    def __lt__(self, other):
        return self.stamina < other.stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
