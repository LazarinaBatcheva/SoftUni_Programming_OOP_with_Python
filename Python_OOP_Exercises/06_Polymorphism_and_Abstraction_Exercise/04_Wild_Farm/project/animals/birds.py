from project.animals.animal import Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def make_sound(self):
        return "Cluck"
