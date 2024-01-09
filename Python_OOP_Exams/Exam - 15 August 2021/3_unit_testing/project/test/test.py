from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.shop = PetShop("Puffy")

    def test_initialization(self):
        self.assertEqual("Puffy", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_attributes_types(self):
        self.assertIsInstance(self.shop.name, str)
        self.assertIsInstance(self.shop.food, dict)
        self.assertIsInstance(self.shop.pets, list)

    def test_add_food_quantity_less_than_or_equal_to_zero_raises(self):
        self.assertEqual({}, self.shop.food)

        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("meat", -1.5)

        expected = "Quantity cannot be equal to or less than 0"
        self.assertEqual({}, self.shop.food)
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("meat", 0)

        expected2 = "Quantity cannot be equal to or less than 0"
        self.assertEqual({}, self.shop.food)
        self.assertEqual(expected2, str(ve.exception))

    def test_add_food_non_existing_name_success(self):
        self.assertEqual({}, self.shop.food)

        result = self.shop.add_food("meat", 300.5)
        expected = "Successfully added 300.50 grams of meat."

        self.assertEqual({"meat": 300.5}, self.shop.food)
        self.assertEqual(expected, result)

    def test_add_food_existing_food_increase_quantity(self):
        self.shop.food = {"meat": 300.5}

        result = self.shop.add_food("meat", 200)
        expected = "Successfully added 200.00 grams of meat."

        self.assertEqual({"meat": 500.5}, self.shop.food)
        self.assertEqual(expected, result)

    def test_add_pet_non_existing_name_success(self):
        self.assertEqual([], self.shop.pets)

        result = self.shop.add_pet("Garfild")
        expected = "Successfully added Garfild."

        self.assertEqual(["Garfild"], self.shop.pets)
        self.assertEqual(expected, result)

    def test_add_pet_existing_name_raises(self):
        self.shop.pets = ["Garfild", "Bob"]

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Bob")

        expected = "Cannot add a pet with the same name"
        self.assertEqual(["Garfild", "Bob"], self.shop.pets)
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_empty_pets_list_raises(self):
        self.assertEqual([], self.shop.pets)

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("meat", "Mike")

        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_non_existing_pet_raises(self):
        self.assertEqual([], self.shop.pets)
        self.shop.add_pet("Bob")
        self.shop.add_pet("Garfild")

        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("meat", "Mike")

        expected = "Please insert a valid pet name"
        self.assertEqual(["Bob", "Garfild"], self.shop.pets)
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_empty_food_dict_failure(self):
        self.assertEqual({}, self.shop.food)
        self.shop.pets = ["Bob"]

        result = self.shop.feed_pet("meat", "Bob")
        expected = "You do not have meat"

        self.assertEqual(expected, result)

    def test_feed_pet_food_quantity_less_than_100_adding_more_food(self):
        self.shop.food = {"meat": 50, "milk": 300}
        self.shop.pets = ["Bob", "Mike"]

        result = self.shop.feed_pet("meat", "Bob")
        expected = "Adding food..."

        self.assertEqual({"meat": 1050, "milk": 300}, self.shop.food)
        self.assertEqual(expected, result)

    def test_feed_pet_food_quantity_more_than_100_food_reduce_with_100(self):
        self.shop.food = {"meat": 50, "milk": 300}
        self.shop.pets = ["Bob", "Mike"]

        result = self.shop.feed_pet("milk", "Mike")
        expected = "Mike was successfully fed"

        self.assertEqual({"meat": 50, "milk": 200}, self.shop.food)
        self.assertEqual(expected, result)

    def test_repr_empty_pets_list(self):
        self.assertEqual("Puffy", self.shop.name)
        self.assertEqual([], self.shop.pets)

        expected = """Shop Puffy:
Pets: """

        self.assertEqual(expected, repr(self.shop))

    def test_repr_existing_pets(self):
        self.assertEqual("Puffy", self.shop.name)
        self.shop.pets = ["Mike", "Bob"]

        expected = """Shop Puffy:
Pets: Mike, Bob"""

        self.assertEqual(expected, repr(self.shop))


if __name__ == "__main__":
    main()
