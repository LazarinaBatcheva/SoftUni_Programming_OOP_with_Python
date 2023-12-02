from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("model", "type", 20_000, 5000.0)

    def test_init(self):
        self.assertEqual("model", self.car.model)
        self.assertEqual("type", self.car.car_type)
        self.assertEqual(20_000, self.car.mileage)
        self.assertEqual(5000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_attributes_types(self):
        self.assertIsInstance(self.car.model, str)
        self.assertIsInstance(self.car.car_type, str)
        self.assertIsInstance(self.car.mileage, int)
        self.assertIsInstance(self.car.price, float)

    def test_setter_price(self):
        self.assertEqual(5000, self.car.price)

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = -1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_setter_mileage(self):
        self.assertEqual(20_000, self.car.mileage)

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 77

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_new_price_greater_than_or_equal_to_old_one_raises(self):
        self.assertEqual(5000, self.car.price)

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5001)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(5000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_new_price_less_than_the_old_one_changed_price(self):
        self.assertEqual(5000, self.car.price)

        result = self.car.set_promotional_price(4500)

        self.assertEqual(4500, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_needed_repair_half_price_of_the_car_less_than_repair_price_returns_impossible_repair_msg(self):
        self.assertEqual(5000, self.car.price)

        result = self.car.need_repair(3000, "repair")

        self.assertEqual(result, "Repair is impossible!")

    def test_needed_repair_half_price_of_the_car_greater_or_equal_to_repair_price_increase_car_price_add_repair(self):
        self.assertEqual(5000, self.car.price)

        result = self.car.need_repair(1000, "repair")

        self.assertEqual(result, "Price has been increased due to repair charges.")
        self.assertEqual(6000, self.car.price)
        self.assertIn("repair", self.car.repairs)

    def test_compare_different_types(self):
        other_car = SecondHandCar("model2", "type2", 10000, 50000.0)

        result = other_car > self.car

        self.assertEqual(result, "Cars cannot be compared. Type mismatch!")

    def test_compare(self):
        other_car = SecondHandCar("model2", "type", 10000, 4000.0)

        result = other_car > self.car

        self.assertFalse(result)

    def test_str(self):
        expected = """Model model | Type type | Milage 20000km
Current price: 5000.00 | Number of Repairs: 0"""

        self.assertEqual(expected, str(self.car))


if __name__ == '__main__':
    main()
