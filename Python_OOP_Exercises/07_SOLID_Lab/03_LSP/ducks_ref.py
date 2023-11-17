from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


# test code
rubber_duck = RubberDuck()
robot_duck = RobotDuck()
print("Rubber Duck says:", rubber_duck.quack())
print("Robot Duck says:", robot_duck.quack())
print("Robot Duck does:", robot_duck.walk())
robot_duck.fly()
print("Robot Duck flies to height:", robot_duck.height)
robot_duck.fly()
print("Robot Duck flies to height:", robot_duck.height)
robot_duck.land()
print("Robot Duck after landing has height:", robot_duck.height)
