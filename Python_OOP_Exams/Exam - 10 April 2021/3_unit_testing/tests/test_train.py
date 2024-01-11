from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("name", 5)

    def test_initialization(self):
        self.assertEqual("name", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_train_is_full_raises(self):
        self.assertEqual(5, self.train.capacity)
        self.train.passengers = ["a", "b", "c", "d", "e"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("q")

        expected = "Train is full"
        self.assertEqual(["a", "b", "c", "d", "e"], self.train.passengers)
        self.assertEqual(expected, str(ve.exception))

    def test_add_passenger_existing_passenger_raises(self):
        self.train.passengers = ["Mike", "Emy"]

        with self.assertRaises(ValueError) as ve:
            result = self.train.add("Emy")

        expected = "Passenger Emy Exists"
        self.assertEqual(expected, str(ve.exception))

    def test_add_passenger_success(self):
        self.assertEqual([], self.train.passengers)

        result = self.train.add("Emy")
        expected = "Added passenger Emy"

        self.assertEqual(["Emy"], self.train.passengers)
        self.assertEqual(expected, result)

        result2 = self.train.add("Mike")
        expected2 = "Added passenger Mike"

        self.assertEqual(["Emy", "Mike"], self.train.passengers)
        self.assertEqual(expected, result)

    def test_remove_passenger_non_existing_passenger_raises(self):
        self.assertEqual([], self.train.passengers)
        self.train.add("Emy")
        self.train.add("Mike")

        with self.assertRaises(ValueError) as ve:
            self.train.remove("John")

        expected = "Passenger Not Found"
        self.assertEqual(["Emy", "Mike"], self.train.passengers)
        self.assertEqual(expected, str(ve.exception))

    def test_remove_passenger_success(self):
        self.assertEqual([], self.train.passengers)
        self.train.add("Emy")
        self.train.add("Mike")

        result = self.train.remove("Emy")
        expected = "Removed Emy"

        self.assertEqual(["Mike"], self.train.passengers)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
