from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(3)

    def test_initialization(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_setter_size_value_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        expected = "Size must be positive number!"
        self.assertEqual(expected, str(ve.exception))

    def test_hire_worker_already_existing_worker_raises(self):
        self.plantation.workers = ["a", "b", "c"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("a")

        expected = "Worker already hired!"
        self.assertEqual(["a", "b", "c"], self.plantation.workers)
        self.assertEqual(expected, str(ve.exception))

    def test_hire_worker_success_returns_msg(self):
        self.assertEqual([], self.plantation.workers)

        result = self.plantation.hire_worker("a")
        expected = "a successfully hired."

        self.assertEqual(["a"], self.plantation.workers)
        self.assertEqual(expected, result)

        result = self.plantation.hire_worker("b")
        expected = "b successfully hired."

        self.assertEqual(["a", "b"], self.plantation.workers)
        self.assertEqual(expected, result)

    def test_len_existing_plants_returns_plants_count(self):
        self.plantation.plants = {"a": ["p1", "p2"], "b": ["p3"]}

        result = len(self.plantation)
        expected = 3

        self.assertEqual(expected, result)

    def test_len_non_existing_plants_returns_0(self):
        self.assertEqual({}, self.plantation.plants)

        result = len(self.plantation)
        expected = 0

        self.assertEqual(expected, result)

    def test_planting_non_existing_workers_raises(self):
        self.plantation.workers = ["a", "b", "c"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("w", "plant")

        expected = "Worker with name w is not hired!"
        self.assertEqual(["a", "b", "c"], self.plantation.workers)
        self.assertEqual(expected, str(ve.exception))

    def test_planting_plants_more_than_plantation_size_raises(self):
        self.plantation.plants = {"a": ["p1", "p2"], "b": ["p3", "p4"]}
        self.plantation.workers = ["a", "b"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("a", "p9")

        expected = "The plantation is full!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_existing_worker_and_empty_space_added_plant_returns_msg(self):
        self.plantation.size = 5
        self.plantation.plants = {"a": ["p1"], "b": ["p2"]}
        self.plantation.workers = ["a", "b"]

        result = self.plantation.planting("a", "p3")
        expected = "a planted p3."

        self.assertEqual({"a": ["p1", "p3"], "b": ["p2"]}, self.plantation.plants)
        self.assertEqual(expected, result)

    def test_planting_non_existing_worker_and_empty_space_added_worker_and_plant_returns_msg(self):
        self.plantation.size = 5
        self.plantation.plants = {"a": ["p1"], "b": ["p2"]}
        self.plantation.workers = ["a", "b", "z"]

        result = self.plantation.planting("z", "p3")
        expected = "z planted it's first p3."

        self.assertEqual({"a": ["p1"], "b": ["p2"], "z": ["p3"]}, self.plantation.plants)
        self.assertEqual(expected, result)

    def test_str(self):
        self.plantation.plants = {"a": ["p1"], "b": ["p2"]}
        self.plantation.workers = ["a", "b", "z"]

        expected = """Plantation size: 3
a, b, z
a planted: p1
b planted: p2"""
        result = str(self.plantation)

        self.assertEqual(expected, result)

    def test_repr(self):
        self.plantation.workers = ["a", "b", "c"]

        expected = """Size: 3
Workers: a, b, c"""
        result = repr(self.plantation)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
