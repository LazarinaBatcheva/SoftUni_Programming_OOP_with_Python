from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def find_robot_by_name(self, robot_name: str):
        return next((r for r in self.robots if r.name == robot_name), None)

    def find_service_by_name(self, service_name: str):
        return next((s for s in self.services if s.name == service_name), None)

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in self.VALID_SERVICES_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICES_TYPES[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in self.VALID_ROBOTS_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        if (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ != "SecondaryService") or \
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ != "MainService"):
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self.find_service_by_name(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.find_service_by_name(service_name)

        fed_robots = [r.eating() for r in service.robots] if service.robots is not None else 0

        return f"Robots fed: {len(fed_robots)}."

    def service_price(self, service_name: str) -> str:
        service = self.find_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service.name} is {total_price:.2f}."

    def __str__(self):
        details_list = [s.details() for s in self.services]

        return "\n". join(details_list)
