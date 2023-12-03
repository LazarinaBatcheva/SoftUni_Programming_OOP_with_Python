from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
        self.robot = Robot("ID", "Education", 10, 1500.0)

    def test_init(self):
        self.assertEqual("ID", self.robot.robot_id)
        self.assertEqual("Education", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(1500.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_attributes_types(self):
        self.assertIsInstance(self.robot.robot_id, str)
        self.assertIsInstance(self.robot.category, str)
        self.assertIsInstance(self.robot.available_capacity, int)
        self.assertIsInstance(self.robot.price, float)

    def test_setter_category(self):
        self.assertEqual("Education", self.robot.category)

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "alabala"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_setter_price(self):
        self.assertEqual(1500.0, self.robot.price)

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_hardware_component_in_hardware_upgrades_returns_not_upgraded_msg(self):
        self.assertEqual([], self.robot.hardware_upgrades)

        self.robot.hardware_upgrades = ["hardware", "upgrade"]

        result = self.robot.upgrade("hardware", 200.0)

        self.assertEqual("Robot ID was not upgraded.", result)

    def test_upgrade_hardware_component_not_in_hardware_upgrades_add_component_increases_price_return_msg(self):
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual(1500.0, self.robot.price)

        result = self.robot.upgrade("hardware", 200.0)

        self.assertIn("hardware", self.robot.hardware_upgrades)
        self.assertEqual(1800.0, self.robot.price)
        self.assertEqual("Robot ID was upgraded with hardware.", result)

    def test_update_software_update_and_version_less_than_highest_software_update(self):
        self.assertEqual([], self.robot.software_updates)

        self.robot.software_updates = [2.0, 3.0, 4.0]

        result = self.robot.update(3.5, 5)

        self.assertEqual("Robot ID was not updated.", result)

    def test_update_software_update_and_version_equal_to_highest_software_update(self):
        self.assertEqual([], self.robot.software_updates)

        self.robot.software_updates = [2.0, 3.0, 4.0]

        result = self.robot.update(4.0, 5)

        self.assertEqual("Robot ID was not updated.", result)

    def test_update_available_capacity_less_than_needed_one(self):
        self.assertEqual(10, self.robot.available_capacity)

        result = self.robot.update(5.0, 12)

        self.assertEqual("Robot ID was not updated.", result)

    def test_update_highest_version_and_enough_capacity_add_version_decrease_capacity_returns_msg(self):
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(10, self.robot.available_capacity)

        result = self.robot.update(5.0, 5)

        self.assertIn(5.0, self.robot.software_updates)
        self.assertEqual(5.0, self.robot.available_capacity)
        self.assertEqual("Robot ID was updated to version 5.0.", result)

    def test_compare_robot_price_greater_than_other_robot_price(self):
        self.assertEqual(1500.0, self.robot.price)
        robot2 = Robot("id2", "Military", 5, 1000.0)

        result = self.robot > robot2

        self.assertEqual(result, "Robot with ID ID is more expensive than Robot with ID id2.")

    def test_compare_robot_price_equal_to_other_robot_price(self):
        self.assertEqual(1500.0, self.robot.price)
        robot2 = Robot("id2", "Military", 5, 1500.0)

        result = self.robot > robot2

        self.assertEqual(result, "Robot with ID ID costs equal to Robot with ID id2.")

    def test_compare_robot_price_less_than_other_robot_price(self):
        self.assertEqual(1500.0, self.robot.price)
        robot2 = Robot("id2", "Military", 5, 2000.0)

        result = self.robot > robot2

        self.assertEqual(result, "Robot with ID ID is cheaper than Robot with ID id2.")


if __name__ == '__main__':
    main()
