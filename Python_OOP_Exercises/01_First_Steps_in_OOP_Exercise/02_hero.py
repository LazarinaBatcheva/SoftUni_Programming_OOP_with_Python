class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        if self.health - damage <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        self.health -= damage

    def heal(self, amount: int):
        self.health += amount


# test
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

