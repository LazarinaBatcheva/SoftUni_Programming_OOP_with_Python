from unittest import TestCase, main

from extended_list import IntegerList


class IntegerListTests(TestCase):
    def setUp(self):
        self.integers_list = IntegerList(
            "1.5",
            1,
            2.5,
            2,
            False,
            3,
            "1"
        )

    def test_correct_init_and_get_data(self):
        self.assertEqual([1, 2, 3], self.integers_list.get_data())

    def test_add_non_integer_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integers_list.add(1.3)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_to_the_list(self):
        self.integers_list.add(4)

        self.assertEqual([1, 2, 3, 4], self.integers_list.get_data())

    def test_remove_or_get_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie2:
            self.integers_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ie2.exception))

    def test_remove_element_with_valid_index(self):
        expected_element = self.integers_list.get_data()[2]

        self.integers_list.remove_index(2)

        self.assertEqual([1, 2], self.integers_list.get_data())
        self.assertEqual(3, expected_element)

    def test_get_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie2:
            self.integers_list.get(4)

        self.assertEqual("Index is out of range", str(ie2.exception))

    def test_get_element_with_valid_index(self):
        expected_element = self.integers_list.get_data()[2]

        self.integers_list.get(2)

        self.assertEqual(3, expected_element)

    def test_insert_element_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers_list.insert(3, 0)

        self.assertEqual("Index is out of range", str(ie.exception))

        with self.assertRaises(IndexError) as ie2:
            self.integers_list.insert(4, 0)

        self.assertEqual("Index is out of range", str(ie2.exception))

    def test_insert_non_integer_element_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integers_list.insert(0, 2.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_element_with_valid_index(self):
        self.integers_list.insert(0, 7)

        self.assertEqual([7, 1, 2, 3], self.integers_list.get_data())

    def test_get_biggest_integer(self):
        self.assertEqual(3, self.integers_list.get_biggest())

    def test_get_index_of_element_from_the_list(self):
        expected_element = self.integers_list.get_data().index(1)

        self.integers_list.get_index(1)

        self.assertEqual(0, expected_element)


if __name__ == '__main__':
    main()
