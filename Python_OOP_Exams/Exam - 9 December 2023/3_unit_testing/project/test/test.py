from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("name")

    def test_initialization(self):
        self.assertEqual("name", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_setter_name_less_than_or_equal_to_3_char_raises(self):
        self.assertEqual("name", self.station.name)

        with self.assertRaises(ValueError) as ve:
            self.station.name = "abc"

        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.station.name = "ab"

        expected = "Name should be more than 3 symbols!"
        self.assertEqual(expected, str(ve.exception))

    def test_new_arrival_on_board_added_new_train_info(self):
        self.assertEqual(deque(), self.station.arrival_trains)

        self.station.new_arrival_on_board("train")

        self.assertEqual(deque(["train"]), self.station.arrival_trains)

        self.station.new_arrival_on_board("abc")
        self.assertEqual(deque(["train", "abc"]), self.station.arrival_trains)

    def test_train_has_arrived_existing_trains_first_train_not_same_with_the_given_one(self):
        self.station.arrival_trains = deque(["train", "abc"])

        result = self.station.train_has_arrived("some")
        expected = "There are other trains to arrive before some."

        self.assertEqual(expected, result)

    def test_train_has_arrived_non_existing_trains(self):
        self.assertEqual(deque(), self.station.arrival_trains)

        result = self.station.train_has_arrived("some")
        expected = "There are other trains to arrive before some."

        self.assertEqual(expected, result)

    def test_train_has_arrived_existing_trains_first_train_same_with_the_given_one(self):
        self.assertEqual(deque(), self.station.departure_trains)
        self.station.arrival_trains = deque(["train", "abc"])

        result = self.station.train_has_arrived("train")
        expected = "train is on the platform and will leave in 5 minutes."

        self.assertEqual(deque(["abc"]), self.station.arrival_trains)
        self.assertEqual(deque(["train"]), self.station.departure_trains)
        self.assertEqual(expected, result)

    def test_train_has_left_if_existing_departure_trains_returns_true_or_false(self):
        self.assertEqual(deque(), self.station.departure_trains)

        result = self.station.train_has_left("abc")

        self.assertFalse(result)

        self.station.departure_trains = deque(["abc", "train"])

        result = self.station.train_has_left("abc")

        self.assertTrue(result)

    def test_train_has_left_if_existing_departure_trains_but_first_not_same(self):
        self.assertEqual(deque(), self.station.departure_trains)

        self.station.departure_trains = deque(["abc", "train"])

        result = self.station.train_has_left("train")

        self.assertFalse(result)

    def test_train_has_left_with_empty_departure_trains(self):
        self.assertEqual(deque(), self.station.departure_trains)
        result = self.station.train_has_left("train")
        self.assertFalse(result)


if __name__ == '__main__':
    main()
