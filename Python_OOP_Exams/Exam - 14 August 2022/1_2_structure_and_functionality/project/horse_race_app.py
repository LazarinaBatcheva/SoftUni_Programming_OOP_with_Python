from typing import Any

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    @staticmethod
    def find_obj(searching_el, searching_attribute: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attribute) == searching_el), None)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str:
        if horse_type in self.VALID_HORSE_TYPES:
            horse = self.find_obj(horse_name, "name", self.horses)

            if horse is not None:
                raise Exception(f"Horse {horse_name} has been already added!")

            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        jockey = self.find_obj(jockey_name, "name", self.jockeys)
        if jockey is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        race = self.find_obj(race_type, "race_type", self.horse_races)
        if race is not None:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str:
        if horse_type not in self.VALID_HORSE_TYPES:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        horse_class = self.VALID_HORSE_TYPES[horse_type]

        jockey = self.find_obj(jockey_name, "name", self.jockeys)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for h_obj in self.horses[::-1]:
            if isinstance(h_obj, horse_class) and not h_obj.is_taken:
                if jockey.horse:
                    return f"Jockey {jockey_name} already has a horse."

                jockey.horse = h_obj
                h_obj.is_taken = True
                return f"Jockey {jockey_name} will ride the horse {h_obj.name}."

        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        race = self.find_obj(race_type, "race_type", self.horse_races)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_obj(jockey_name, "name", self.jockeys)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> str:
        race = self.find_obj(race_type, "race_type", self.horse_races)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(self.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_speed = 0
        horse_winner = None
        jockey_winner = ""

        for jockey in self.jockeys:
            horse = jockey.horse
            if horse.speed > winner_speed:
                winner_speed = horse.speed
                horse_winner = horse
                jockey_winner = jockey.name

        return (f"The winner of the {race_type} race, "
                f"with a speed of {winner_speed}km/h is {jockey_winner}! "
                f"Winner's horse: {horse_winner.name}.")
