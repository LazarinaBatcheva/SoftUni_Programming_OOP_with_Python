from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.shelf = ToyStore()

    def test_initialization(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

    def test_add_toy_non_existing_shelf_raises(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("Q", "car")
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_existing_same_toy_on_shelf_raises(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        self.shelf.toy_shelf["A"] = "car"

        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("A", "car")
        self.assertEqual({
            "A": "car",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_existing_other_toy_on_shelf_raises(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        self.shelf.toy_shelf["A"] = "car"

        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("A", "truck")
        self.assertEqual({
            "A": "car",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_success(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        result = self.shelf.add_toy("D", "ball")

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": "ball",
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(result, "Toy:ball placed successfully!")

        result = self.shelf.add_toy("A", "bear")

        self.assertEqual({
            "A": "bear",
            "B": None,
            "C": None,
            "D": "ball",
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(result, "Toy:bear placed successfully!")

    def test_remove_toy_non_existing_shelf_raises(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        self.shelf.add_toy("A", "car")
        self.shelf.add_toy("B", "bear")
        self.shelf.add_toy("C", "truck")

        with self.assertRaises(Exception) as ex:
            self.shelf.remove_toy("W", "wolf")
        self.assertEqual({
            "A": "car",
            "B": "bear",
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_different_toy_raises(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        self.shelf.add_toy("A", "car")
        self.shelf.add_toy("B", "bear")
        self.shelf.add_toy("C", "truck")

        with self.assertRaises(Exception) as ex:
            self.shelf.remove_toy("A", "ball")
        self.assertEqual({
            "A": "car",
            "B": "bear",
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_success(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

        self.shelf.add_toy("A", "car")
        self.shelf.add_toy("B", "bear")
        self.shelf.add_toy("C", "truck")

        result = self.shelf.remove_toy("B", "bear")

        self.assertEqual({
            "A": "car",
            "B": None,
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)
        self.assertEqual(result, "Remove toy:bear successfully!")


if __name__ == '__main__':
    main()
