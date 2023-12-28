from typing import Any, Optional

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: list[Car] = []
        self.drivers: list[Driver] = []
        self.races: list[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> Optional[str]:
        if car_type not in self.VALID_CAR_TYPES:
            return

        car = self.__find_obj(model, "model", self.cars)

        if car is not None:
            raise Exception(f"Car {model} is already created!")

        new_car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        driver = self.__find_obj(driver_name, "name", self.drivers)

        if driver is not None:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        race = self.__find_obj(race_name, "name", self.races)

        if race is not None:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        driver = self.__find_obj(driver_name, "name", self.drivers)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__take_last_car_by_type(car_type)

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        msg = ""
        if driver.car is not None:
            previous_car = driver.car
            previous_car.is_taken = False
            driver.car = None
            msg += f"Driver {driver_name} changed his car from {previous_car.model} to {car.model}."
        else:
            msg += f"Driver {driver_name} chose the car {car.model}."

        driver.car = car
        car.is_taken = True

        return msg

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        race = self.__find_obj(race_name, "name", self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_obj(driver_name, "name", self.drivers)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_obj(race_name, "name", self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = []
        count = 0

        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit):
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
            count += 1
            if count == 3:
                break

        return "\n".join(result)

    # HELPERS
    @staticmethod
    def __find_obj(searching_el, searching_attr: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attr) == searching_el), None)

    def __take_last_car_by_type(self, car_type):
        return next((c for c in reversed(self.cars) if c.__class__.__name__ == car_type and not c.is_taken), None)
