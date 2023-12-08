from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCard(TestCase):
    def setUp(self):
        self.shop = ShoppingCart("Guess", 200.0)

    def test_initialization(self):
        self.assertEqual("Guess", self.shop.shop_name)
        self.assertEqual(200.0, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_attributes_types(self):
        self.assertIsInstance(self.shop.shop_name, str)
        self.assertIsInstance(self.shop.budget, float)

    def test_setter_shop_name_not_start_with_upper_letter_and_not_only_letters_raises(self):
        self.assertEqual("Guess", self.shop.shop_name)

        result = "Shop must contain only letters and must start with capital letter!"

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "guess"
        self.assertEqual(str(ve.exception), result)

        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "Guess7"
        self.assertEqual(str(ve.exception), result)

    def test_add_to_cart_given_price_equal_to_or_greater_than_100_raises(self):
        self.assertEqual({}, self.shop.products)

        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("dress", 100.0)
        self.assertEqual({}, self.shop.products)
        self.assertEqual(str(ve.exception), "Product dress cost too much!")

        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("bag", 101.0)
        self.assertEqual({}, self.shop.products)
        self.assertEqual(str(ve.exception), "Product bag cost too much!")

    def test_add_to_cart_product_price_less_than_100_added_product_with_price_returns_msg(self):
        self.assertEqual({}, self.shop.products)

        result = self.shop.add_to_cart("dress", 90.0)

        self.assertEqual({"dress": 90.0}, self.shop.products)
        self.assertEqual(result, "dress product was successfully added to the cart!")

        result = self.shop.add_to_cart("bag", 70.0)

        self.assertEqual({"dress": 90.0, "bag": 70.0}, self.shop.products)
        self.assertEqual(result, "bag product was successfully added to the cart!")

    def test_remove_from_cart_product_name_not_in_products_raises(self):
        self.assertEqual({}, self.shop.products)

        self.shop.add_to_cart("coat", 99.0)
        self.shop.add_to_cart("pants", 50.0)

        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("hat")
        self.assertEqual({"coat": 99.0, "pants": 50.0}, self.shop.products)
        self.assertEqual(str(ve.exception), "No product with name hat in the cart!")

    def test_remove_from_cart_existing_product_name_product_removed_returns_msg(self):
        self.assertEqual({}, self.shop.products)

        self.shop.add_to_cart("hat", 25.0)
        self.shop.add_to_cart("dress", 89.0)
        self.shop.add_to_cart("coat", 92.0)

        result = self.shop.remove_from_cart("hat")

        self.assertEqual({"dress": 89.0, "coat": 92.0}, self.shop.products)
        self.assertEqual(result, "Product hat was successfully removed from the cart!")

    def test_add_new_cart(self):
        self.assertEqual("Guess", self.shop.shop_name)
        self.assertEqual(200.0, self.shop.budget)

        new_shop = ShoppingCart("New", 100.0)

        self.shop.add_to_cart("hat", 20.0)
        new_shop.add_to_cart("bag", 40.0)

        new_shop = self.shop + new_shop

        self.assertEqual("GuessNew", new_shop.shop_name)
        self.assertEqual(300.0, new_shop.budget)
        self.assertEqual({"hat": 20.0, "bag": 40.0}, new_shop.products)

    def test_bye_product_total_products_sum_greater_than_budget_raises(self):
        self.assertEqual(200.0, self.shop.budget)
        self.assertEqual({}, self.shop.products)

        self.shop.add_to_cart("dress", 90.0)
        self.shop.add_to_cart("coat", 90.0)
        self.shop.add_to_cart("pants", 80)

        result = "Not enough money to buy the products! Over budget with 60.00lv!"

        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        self.assertEqual(str(ve.exception), result)

    def test_bye_product_success_returns_msg(self):
        self.assertEqual(200.0, self.shop.budget)
        self.assertEqual({}, self.shop.products)

        self.shop.add_to_cart("dress", 90.0)
        self.shop.add_to_cart("coat", 90.0)

        result = self.shop.buy_products()
        
        self.assertEqual(result, "Products were successfully bought! Total cost: 180.00lv.")


if __name__ == '__main__':
    main()
