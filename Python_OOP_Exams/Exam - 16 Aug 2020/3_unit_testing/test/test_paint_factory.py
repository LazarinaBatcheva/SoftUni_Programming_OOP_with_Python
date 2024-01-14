from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("name", 100)

    def test_initialization(self):
        self.assertEqual("name", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient_invalid_ingredient_type_raises(self):
        self.assertEqual({}, self.factory.ingredients)

        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("black", 50)

        expected = "Ingredient of type black not allowed in PaintFactory"
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(expected, str(te.exception))

    def test_add_ingredient_valid_ingredient_type_not_enough_capacity_raises(self):
        self.assertEqual({}, self.factory.ingredients)

        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 101)

        expected = "Not enough space in factory"
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(expected, str(ve.exception))

    def test_add_ingredient_valid_ingredient_type_boundary_capacity(self):
        self.assertEqual({}, self.factory.ingredients)

        self.factory.add_ingredient("white", 100)

        self.assertEqual({"white": 100}, self.factory.ingredients)

    def test_add_ingredient_non_existing_product_success(self):
        self.assertEqual({}, self.factory.ingredients)

        self.factory.add_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.factory.ingredients)

        self.factory.add_ingredient("blue", 10)
        self.assertEqual({"white": 10, "blue": 10}, self.factory.ingredients)

    def test_add_ingredient_existing_product_increases_quantity(self):
        self.factory.ingredients = {"blue": 10, "red": 20}

        self.factory.add_ingredient("red", 10)

        self.assertEqual({"blue": 10, "red": 30}, self.factory.ingredients)

    def test_remove_ingredient_non_existing_product_raises(self):
        self.assertEqual({}, self.factory.ingredients)

        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("red", 10)

        expected = "No such ingredient in the factory"
        self.assertEqual(expected, str(ke.exception))

        self.factory.ingredients = {"red": 10, "blue": 10}

        with self.assertRaises(KeyError) as ke2:
            self.factory.remove_ingredient("white", 10)

        self.assertEqual(expected, str(ke2.exception))

    def test_remove_ingredient_too_much_given_quantity_raises(self):
        self.factory.ingredients = {"red": 10, "blue": 20}

        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("red", 11)

        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual({"red": 10, "blue": 20}, self.factory.ingredients)
        self.assertEqual(expected, str(ve.exception))

    def test_remove_ingredient_boundary_quantity(self):
        self.factory.ingredients = {"red": 10, "blue": 20}

        self.factory.remove_ingredient("red", 10)

        self.assertEqual({"red": 0, "blue": 20}, self.factory.ingredients)

    def test_property_products(self):
        self.assertEqual({}, self.factory.ingredients)

        self.factory.add_ingredient("red", 10)

        self.assertEqual({"red": 10}, self.factory.products)

    def test_can_add_failure(self):
        self.assertEqual(100, self.factory.capacity)

        self.factory.ingredients = {"red": 50, "white": 50}

        self.assertFalse(self.factory.can_add(2))

    def test_can_add_success(self):
        self.assertEqual(100, self.factory.capacity)

        self.factory.ingredients = {"red": 10, "white": 50}

        self.assertTrue(self.factory.can_add(10))

    def test_can_add_boundary_quantity(self):
        self.assertEqual(100, self.factory.capacity)

        self.factory.ingredients = {"red": 40, "white": 50}

        self.assertTrue(self.factory.can_add(10))

    def test_repr_method(self):
        self.factory.ingredients = {"red": 10, "blue": 20}

        expected = """Factory name: name with capacity 100.
red: 10
blue: 20\n"""
        self.assertEqual(expected, repr(self.factory))

    def test_repr_method_existing_ingredients_0_quantities(self):

        self.factory.ingredients = {"red": 0, "blue": 0}

        expected = """Factory name: name with capacity 100.
red: 0
blue: 0\n"""

        self.assertEqual(expected, repr(self.factory))

    def test_repr_method_no_ingredients(self):
        self.assertEqual({}, self.factory.ingredients)

        expected = """Factory name: name with capacity 100.\n"""

        self.assertEqual(expected, repr(self.factory))


if __name__ == '__main__':
    main()
