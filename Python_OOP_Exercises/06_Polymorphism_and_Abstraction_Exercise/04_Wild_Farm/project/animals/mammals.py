from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"
