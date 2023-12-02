from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(10000.0, 2, False)

    def test_init(self):
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertFalse(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_attribute_types(self):
        self.assertIsInstance(self.trip.budget, float)
        self.assertIsInstance(self.trip.travelers, int)
        self.assertIsInstance(self.trip.is_family, bool)

    def test_setter_travelers_less_than_one_raises(self):
        self.assertEqual(2, self.trip.travelers)

        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_setter_is_family(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(2, self.trip.travelers)

        self.trip.travelers = 1
        self.trip.is_family = True

        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_destination_not_in_offers_returns_msg(self):
        result = self.trip.book_a_trip("Greece")

        self.assertEqual("This destination is not in our offers, please choose a new one!", result)

    def test_book_a_trip_not_enough_budget_returns_msg(self):
        self.assertEqual(10000, self.trip.budget)

        result = self.trip.book_a_trip("Australia")

        self.assertEqual("Your budget is not enough!", result)

    def test_book_a_trip_with_family_discount(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

        self.trip.is_family = True

        expected_budget_left = 9100
        result = self.trip.book_a_trip("Bulgaria")

        self.assertTrue(self.trip.is_family)
        self.assertEqual(expected_budget_left, self.trip.budget)
        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 9100.00", result)

    def test_book_a_trip_not_family_discount(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(10000, self.trip.budget)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

        expected_budget_left = 9000
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(expected_budget_left, self.trip.budget)
        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 9000.00", result)

    def test_book_a_trip_family_budget_equal_to_trip_price(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(10000, self.trip.budget)

        self.trip.is_family = True
        self.trip.budget = 900

        result = self.trip.book_a_trip("Bulgaria")

        self.assertTrue(self.trip.is_family)
        self.assertEqual(0, self.trip.budget)
        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 0.00", result)

    def test_book_a_trip_budget_equal_to_trip_price(self):
        self.assertFalse(self.trip.is_family)
        self.assertEqual(10000, self.trip.budget)

        self.trip.budget = 1000

        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual(0, self.trip.budget)
        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 0.00", result)

    def test_booking_status_not_booked_destinations(self):
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(10000, self.trip.budget)

        result = self.trip.booking_status()

        self.assertEqual("No bookings yet. Budget: 10000.00", result)

    def test_booking_status_with_booked_destinations(self):
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(10000, self.trip.budget)

        self.trip.budget = 20000
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("Australia")

        result = self.trip.booking_status()
        expected_result = """Booked Destination: Australia
Paid Amount: 11400.00
Booked Destination: Bulgaria
Paid Amount: 1000.00
Number of Travelers: 2
Budget Left: 7600.00"""

        self.assertIn("Bulgaria", self.trip.booked_destinations_paid_amounts)
        self.assertIn("Australia", self.trip.booked_destinations_paid_amounts)
        self.assertEqual(7600, self.trip.budget)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
