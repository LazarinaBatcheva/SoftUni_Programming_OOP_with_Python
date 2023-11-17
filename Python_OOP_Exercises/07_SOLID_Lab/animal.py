from abc import ABC, abstractmethod
from typing import List, Any


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> Any:
        pass


class Cat(Animal):
    def make_sound(self) -> str:
        return "meow"


class Dog(Animal):
    def make_sound(self) -> str:
        return "woof-woof"


class Chicken(Animal):
    def make_sound(self) -> str:
        return "chicken sound"


class Mouse(Animal):
    def make_sound(self) -> str:
        return "mouse sound"


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


# test code
animals = [Cat(), Dog(), Chicken(), Mouse()]
animal_sound(animals)