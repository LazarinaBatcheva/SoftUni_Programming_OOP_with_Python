import ftplib

from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("Name", 1.2)

    def test_initialization(self):
        self.assertEqual("Name", self.truck_driver.name)
        self.assertEqual(1.2, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_setter_earned_money_less_than_zero_raises(self):
        self.assertEqual(0, self.truck_driver.earned_money)

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money -= 1
        self.assertEqual(str(ve.exception), f"{self.truck_driver.name} went bankrupt.")

    def test_add_cargo_offer_existed_location_raises(self):
        self.assertEqual({}, self.truck_driver.available_cargos)

        self.truck_driver.available_cargos = {"location1": 100, "location2": 110}

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("location1", 20)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_success(self):
        self.assertEqual({}, self.truck_driver.available_cargos)

        result = self.truck_driver.add_cargo_offer("location1", 100)

        self.assertEqual({"location1": 100}, self.truck_driver.available_cargos)
        self.assertEqual(result, "Cargo for 100 to location1 was added as an offer.")

        result = self.truck_driver.add_cargo_offer("location2", 110)
        self.assertEqual({"location1": 100, "location2": 110}, self.truck_driver.available_cargos)
        self.assertEqual(result, "Cargo for 110 to location2 was added as an offer.")

    def test_drive_best_cargo_offer_impossible_with_empty_available_cargos(self):
        self.assertEqual({}, self.truck_driver.available_cargos)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_success_increase_earned_money_and_miles(self):
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

        self.truck_driver.add_cargo_offer("ala bala", 524)
        self.truck_driver.add_cargo_offer("long", 777)
        self.truck_driver.add_cargo_offer("short", 77)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual({"long": 777, "ala bala": 524, "short": 77}, self.truck_driver.available_cargos)
        self.assertEqual(872.4, self.truck_driver.earned_money)
        self.assertEqual(777, self.truck_driver.miles)
        self.assertEqual(result, f"{self.truck_driver.name} is driving 777 to long.")

    def test_test_eat_valid_decreases_earned_money(self):
        self.assertEqual(0, self.truck_driver.earned_money)

        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        expected_earned_money = 80

        self.assertEqual(expected_earned_money, self.truck_driver.earned_money)

    def test_sleep_valid_decreases_earned_money(self):
        self.assertEqual(0, self.truck_driver.earned_money)

        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        expected_earned_money = 55

        self.assertEqual(expected_earned_money, self.truck_driver.earned_money)

    def test_pump_gas_valid_decreases_earned_money(self):
        self.assertEqual(0, self.truck_driver.earned_money)

        self.truck_driver.earned_money = 1000

        self.truck_driver.pump_gas(1500)
        expected_earned_money = 500

        self.assertEqual(expected_earned_money, self.truck_driver.earned_money)

    def test_repair_truck_valid_decreases_earned_money(self):
        self.assertEqual(0, self.truck_driver.earned_money)

        self.truck_driver.earned_money = 10000

        self.truck_driver.repair_truck(10000)
        expected_earned_money = 2500

        self.assertEqual(expected_earned_money, self.truck_driver.earned_money)

    def test_represent(self):
        self.assertEqual(0, self.truck_driver.miles)

        self.truck_driver.miles = 100
        expected = f"{self.truck_driver.name} has {self.truck_driver.miles} miles behind his back."

        result = self.truck_driver.__repr__()

        self.assertEqual(100, self.truck_driver.miles)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
