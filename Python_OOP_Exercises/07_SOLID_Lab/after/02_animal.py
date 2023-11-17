from abc import ABC, abstractmethod
from typing import List, Any


class Animal(ABC):
    @staticmethod
    @abstractmethod
    def make_sound() -> Any:
        pass


class Cat(Animal):
    @staticmethod
    def make_sound() -> str:
        return "meow"


class Dog(Animal):
    @staticmethod
    def make_sound() -> str:
        return "woof-woof"


class Chicken(Animal):
    @staticmethod
    def make_sound() -> str:
        return "chicken sound"


class Mouse(Animal):
    @staticmethod
    def make_sound() -> str:
        return "mouse sound"


def animal_sound(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


# test code
animals = [Cat(), Dog(), Chicken(), Mouse()]
animal_sound(animals)
