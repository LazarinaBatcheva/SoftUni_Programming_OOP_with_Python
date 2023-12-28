from unittest import TestCase, main

from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Indoor", "hands", 100, 100)

    def test_initialization(self):
        self.assertEqual("Indoor", self.robot.category)
        self.assertEqual("hands", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.robot.ALLOWED_CATEGORIES)

    def test_attributes_types(self):
        self.assertIsInstance(self.robot.category, str)
        self.assertIsInstance(self.robot.part_type, str)
        self.assertIsInstance(self.robot.capacity, int)
        self.assertIsInstance(self.robot.memory, int)
        self.assertIsInstance(self.robot.ALLOWED_CATEGORIES, list)
        self.assertIsInstance(self.robot.installed_software, list)

    def test_setter_not_allowed_category_raises(self):
        self.assertEqual("Indoor", self.robot.category)

        with self.assertRaises(ValueError) as ve:
            self.robot.category = "category"
        expected = f"Category should be one of {self.robot.ALLOWED_CATEGORIES}"
        self.assertEqual(expected, str(ve.exception))

    def test_get_used_capacity(self):
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(0, self.robot.get_used_capacity())

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        self.robot.install_software(software)
        self.assertEqual(50, self.robot.get_used_capacity())

        software2 = {"name": "name2", "capacity_consumption": 10, "memory_consumption": 50}
        self.robot.install_software(software2)
        self.assertEqual(60, self.robot.get_used_capacity())

    def test_get_available_capacity(self):
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.get_available_capacity())

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        self.robot.install_software(software)
        self.assertEqual(50, self.robot.get_available_memory())

    def test_get_used_memory(self):
        self.assertEqual(100, self.robot.memory)
        self.assertEqual(0, self.robot.get_used_memory())

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        self.robot.install_software(software)
        self.assertEqual(50, self.robot.get_used_memory())

    def test_get_available_memory(self):
        self.assertEqual(100, self.robot.memory)
        self.assertEqual(100, self.robot.get_available_memory())

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        self.robot.install_software(software)
        self.assertEqual(50, self.robot.get_available_memory())

    def test_install_software_success(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        result = self.robot.install_software(software)
        expected = "Software 'name' successfully installed on Indoor part."

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(50, self.robot.get_available_capacity())
        self.assertEqual(50, self.robot.get_available_memory())

        # Testing using full capacity
        software = {"name": "other name", "capacity_consumption": 50, "memory_consumption": 50}
        result = self.robot.install_software(software)
        expected = "Software 'other name' successfully installed on Indoor part."

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(0, self.robot.get_available_capacity())
        self.assertEqual(0, self.robot.get_available_memory())

    def test_install_software_take_more_capacity_second_time_failure(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 50}
        result = self.robot.install_software(software)
        expected = "Software 'name' successfully installed on Indoor part."

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(50, self.robot.get_available_capacity())
        self.assertEqual(50, self.robot.get_available_memory())

        software2 = {"name": "other name", "capacity_consumption": 100, "memory_consumption": 50}
        result2 = self.robot.install_software(software2)
        expected2 = "Software 'other name' cannot be installed on Indoor part."

        self.assertNotIn(software2, self.robot.installed_software)
        self.assertEqual(expected2, result2)
        self.assertEqual(50, self.robot.get_available_capacity())
        self.assertEqual(50, self.robot.get_available_memory())

    def test_install_software_boundary_condition(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 100, "memory_consumption": 100}
        result = self.robot.install_software(software)
        expected = "Software 'name' successfully installed on Indoor part."

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(0, self.robot.get_available_capacity())
        self.assertEqual(0, self.robot.get_available_memory())

    def test_install_software_less_capacity(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 150, "memory_consumption": 50}
        result = self.robot.install_software(software)
        expected = "Software 'name' cannot be installed on Indoor part."

        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(100, self.robot.get_available_capacity())
        self.assertEqual(100, self.robot.get_available_memory())

    def test_install_software_less_memory(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 50, "memory_consumption": 150}
        result = self.robot.install_software(software)
        expected = "Software 'name' cannot be installed on Indoor part."

        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(100, self.robot.get_available_capacity())
        self.assertEqual(100, self.robot.get_available_memory())

    def test_install_software_less_capacity_and_memory(self):
        self.assertEqual([], self.robot.installed_software)

        software = {"name": "name", "capacity_consumption": 150, "memory_consumption": 150}
        result = self.robot.install_software(software)
        expected = "Software 'name' cannot be installed on Indoor part."

        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(expected, result)
        self.assertEqual(100, self.robot.get_available_capacity())
        self.assertEqual(100, self.robot.get_available_memory())



if __name__ == '__main__':
    main()
