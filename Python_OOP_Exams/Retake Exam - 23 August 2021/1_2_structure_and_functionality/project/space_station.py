from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {"Biologist": Biologist,
                             "Geodesist": Geodesist,
                             "Meteorologist": Meteorologist}
    successful_missions = 0
    not_completed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        # Check if the astronaut already exists in the repository
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        # Create a new astronaut object of the specified type and add it to the repository
        new_astronaut = self.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        # Check if the planet already exists in the repository
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        # Create a new planet object and adding items string into a list
        new_planet = Planet(name)
        new_planet.items = items.split(", ")

        # Add the new planet to the repository
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)

        # Check if the astronaut doesn't exist in the repository
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        # Retiring astronaut from the space station by removing from the repository
        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        # Increasing the oxygen of each astronaut
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str) -> str:
        planet = self.planet_repository.find_by_name(planet_name)

        # Check if planet doesn't exist
        if planet is None:
            raise Exception("Invalid planet name!")

        # Search for suitable astronauts
        suitable_astronauts = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda a: -a.oxygen)
                               if a.oxygen > 30]

        # Check if there aren't any suitable astronauts
        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astronauts = suitable_astronauts[:5] if len(suitable_astronauts) > 5 else suitable_astronauts
        astronauts_who_participated = 0

        for astronaut in suitable_astronauts:
            while astronaut.oxygen > 0 and planet.items:
                astronaut.breathe()
                astronaut.backpack.append(planet.items.pop())
            astronauts_who_participated += 1

            if not planet.items:
                # All items collected, mission successful
                self.successful_missions += 1
                return (f"Planet: {planet_name} was explored. "
                        f"{astronauts_who_participated} astronauts participated in collecting items.")

        # Not all items were collected, mission is not completed
        self.not_completed_missions += 1
        return f"Mission is not completed."

    def report(self) -> str:
        report_lines = []

        report_lines.append(f"{self.successful_missions} successful missions!")
        report_lines.append(f"{self.not_completed_missions} missions were not completed!")
        report_lines.append("Astronauts' info:")

        astronaut_info = [str(a) for a in self.astronaut_repository.astronauts]

        report_lines.extend(astronaut_info)

        return "\n".join(report_lines)
