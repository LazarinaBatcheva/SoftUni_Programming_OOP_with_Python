from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_TYPES_OF_VEHICLES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def get_user_by_driving_license_number(self, driver_license_number: str):
        return next((u for u in self.users
                     if u.driving_license_number == driver_license_number), None)

    def get_vehicle_by_license_plate_number(self, license_plate_number: str):
        return next((v for v in self.vehicles
                     if v.license_plate_number == license_plate_number), None)

    def get_route_by_start_point_end_point(self, start_point: str, end_point: str):
        return next((r for r in self.routes
                     if r.start_point == start_point and r.end_point == end_point), None)

    def get_route_by_route_id(self, route_id: int):
        return next((r for r in self.routes if r.route_id == route_id), None)

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        existing_user = self.get_user_by_driving_license_number(driving_license_number)

        if existing_user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in self.VALID_TYPES_OF_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        existing_vehicle = self.get_vehicle_by_license_plate_number(license_plate_number)

        if existing_vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VALID_TYPES_OF_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        new_route_id = len(self.routes) + 1

        existing_route = self.get_route_by_start_point_end_point(start_point, end_point)

        if existing_route:
            if existing_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif existing_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            else:
                existing_route.is_locked = True

        new_route = Route(start_point, end_point, length, new_route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.get_user_by_driving_license_number(driving_license_number)
        vehicle = self.get_vehicle_by_license_plate_number(license_plate_number)
        route = self.get_route_by_route_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
        sorted_damaged_vehicles = sorted_damaged_vehicles[:count]

        for v in sorted_damaged_vehicles:
            v.change_status()
            v.recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)

        result = ["*** E-Drive-Rent ***"]
        result.extend(str(u) for u in sorted_users)

        return "\n".join(result)
