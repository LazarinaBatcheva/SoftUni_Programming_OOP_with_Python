from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    # for air condition fuel increases by 0.9 liters
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int) -> float:
        fuel_needed = distance * (self.fuel_consumption + 0.9)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            return self.fuel_quantity

    def refuel(self, fuel: int) -> float:
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    # for air condition fuel increases by 1.6 liters
    # refuel 95% of fuel tank
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            return self.fuel_quantity

    def refuel(self, fuel: int):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity


# test code
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print()
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

