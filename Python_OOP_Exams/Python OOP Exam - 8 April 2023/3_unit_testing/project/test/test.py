from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Novak", 36, 100.)

    def test_init(self):
        self.assertEqual("Novak", self.player.name)
        self.assertEqual(36, self.player.age)
        self.assertEqual(100., self.player.points)
        self.assertEqual([], self.player.wins)

    def test_attributes_types(self):
        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.age, int)
        self.assertIsInstance(self.player.points, float)

    def test_setter_name_characters_les_than_or_equal_to_two_raises(self):
        self.assertEqual("Novak", self.player.name)

        with self.assertRaises(ValueError) as ve:
            self.player.name = "No"
        expected = "Name should be more than 2 symbols!"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = "N"
        expected_ = "Name should be more than 2 symbols!"
        self.assertEqual(expected_, str(ve.exception))

    def test_setter_age_less_than_18_raises(self):
        self.assertEqual(36, self.player.age)

        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        expected = "Players must be at least 18 years of age!"
        self.assertEqual(expected, str(ve.exception))

    def test_setter_age_equal_to_18(self):
        self.assertEqual(36, self.player.age)

        self.player.age = 18

        self.assertEqual(18, self.player.age)

    def test_add_not_existing_tournament_name_in_wins(self):
        self.assertEqual([], self.player.wins)

        self.player.add_new_win("US Open")

        # self.assertIn("US Open", self.player.wins)
        self.assertEqual(["US Open"], self.player.wins)

    def test_add_existing_tournament_name_returns_already_added_tournament_name_msg(self):
        self.assertEqual([], self.player.wins)

        self.player.add_new_win("US Open")
        self.player.add_new_win("Some")

        result = self.player.add_new_win("Some")

        # self.assertIn("Some", self.player.wins)
        self.assertEqual(["US Open", "Some"], self.player.wins)
        expected = "Some has been already added to the list of wins!"
        self.assertEqual(expected, result)

    def test_player_points_less_than_the_other_player(self):
        self.assertEqual(100., self.player.points)
        player2 = TennisPlayer("Grisho", 30, 110.)

        result = self.player < player2

        expected = f"{player2.name} is a top seeded player and he/she is better than {self.player.name}"
        self.assertEqual(expected, result)

    def test_player_points_more_than_or_equal_to_the_other_player(self):
        self.assertEqual(100., self.player.points)
        player2 = TennisPlayer("Grisho", 30, 100.)

        result = self.player < player2

        expected = f"{self.player.name} is a better player than {player2.name}"
        self.assertEqual(expected, result)

        player2.points = 90.
        result = self.player < player2

        expected_ = f"{self.player.name} is a better player than {player2.name}"
        self.assertEqual(expected_, result)

    def test_str_represent(self):
        expected = """Tennis Player: Novak
Age: 36
Points: 100.0
Tournaments won: """

        self.assertEqual(expected, str(self.player))

        self.player.add_new_win("US Open")
        self.player.add_new_win("Some")

        expected_with = """Tennis Player: Novak
Age: 36
Points: 100.0
Tournaments won: US Open, Some"""

        self.assertEqual(expected_with, str(self.player))


if __name__ == "__main__":
    main()
