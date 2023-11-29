from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    # fuel = 50.5
    # horse_power = 100.5

    def setUp(self):
        self.test_vehicle = Vehicle(50.5, 100.5)

    def test_init(self):
        self.assertEqual(50.5, self.test_vehicle.fuel)
        self.assertEqual(50.5, self.test_vehicle.capacity)
        self.assertEqual(100.5, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)

    def test_drive_when_fuel_is_less_than_fuel_needed_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_fuel_enough(self):
        self.test_vehicle.drive(10)
        expected_fuel = 38

        self.assertEqual(expected_fuel, self.test_vehicle.fuel)

    def test_refuel_when_fuel_became_more_than_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_vehicle.fuel = 40.5

            self.test_vehicle.refuel(20)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.test_vehicle.fuel = 40.5

        self.test_vehicle.refuel(5)

        self.assertEqual(45.5, self.test_vehicle.fuel)

    def test_str_represent(self):
        self.test_vehicle.fuel = 30.5

        expected = (f"The vehicle has {self.test_vehicle.horse_power} "
                    f"horse power with {self.test_vehicle.fuel} fuel left and "
                    f"{self.test_vehicle.fuel_consumption} fuel consumption")

        self.assertEqual(expected, str(self.test_vehicle))


if __name__ == '__main__':
    main()
