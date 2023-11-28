from unittest import TestCase, main

from car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car_manager = Car("Toyota", "Corolla", 5, 50)

    def test_correct_init(self):
        self.assertEqual("Toyota", self.car_manager.make)
        self.assertEqual("Corolla", self.car_manager.model)
        self.assertEqual(5, self.car_manager.fuel_consumption)
        self.assertEqual(50, self.car_manager.fuel_capacity)
        self.assertEqual(0, self.car_manager.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Corolla", 5, 50)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Toyota", "", 5, 50)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_zero_or_less_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Toyota", "Corolla", 0, 50)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex2:
            car = Car("Toyota", "Corolla", -1, 50)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex2.exception))

    def test_fuel_capacity_is_zero_or_less_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Toyota", "Corolla", 5, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex2:
            car = Car("Toyota", "Corolla", 5, -1)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex2.exception))

    def test_fuel_amount_is_less_than_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_fuel_or_less_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex2:
            self.car_manager.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex2.exception))

    def test_increasing_fuel_amount_with_given_fuel(self):
        self.car_manager.fuel_amount = 10

        self.car_manager.refuel(10)
        expected_fuel_amount = 20

        self.assertEqual(expected_fuel_amount, self.car_manager.fuel_amount)

    def test_fuel_amount_became_more_than_fuel_capacity_fuel_amount_equal_to_fuel_capacity(self):
        self.car_manager.fuel_amount = 40

        self.car_manager.refuel(20)
        expected_fuel_amount = 50

        self.assertEqual(expected_fuel_amount, self.car_manager.fuel_amount)

    def test_drive_fuel_needed_more_than_fuel_amount_raises_exception(self):
        self.car_manager.fuel_amount = 30

        with self.assertRaises(Exception) as ex:
            self.car_manager.drive(800)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_fuel_amount_decreases_with_fuel_needed(self):
        self.car_manager.fuel_amount = 40

        self.car_manager.drive(100)
        expected_fuel_amount = 35

        self.assertEqual(expected_fuel_amount, self.car_manager.fuel_amount)


if __name__ == '__main__':
    main()
