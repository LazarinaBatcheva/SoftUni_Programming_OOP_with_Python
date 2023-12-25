from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("name", 2000, 1.5)

    def test_initialization(self):
        self.assertEqual("name", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(1.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_setter_name_empty_string_raises(self):
        self.assertEqual("name", self.movie.name)

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_setter_year_less_than_1887_raises(self):
        self.assertEqual(2000, self.movie.year)

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        expected = "Year is not valid!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_actor_existed_name_returns_impossible_adding_msg(self):
        self.assertEqual([], self.movie.actors)
        self.movie.actors = ["name1", "name2"]

        result = self.movie.add_actor("name1")
        expected = "name1 is already added in the list of actors!"

        self.assertEqual(expected, result)

    def test_add_actor_not_existing_name_successfully(self):
        self.assertEqual([], self.movie.actors)

        result = self.movie.add_actor("name1")
        self.assertEqual(["name1"], self.movie.actors)

        result = self.movie.add_actor("name2")
        self.assertEqual(["name1", "name2"], self.movie.actors)

    def test_movie_rating_greater_than_the_other_one(self):
        self.assertEqual(1.5, self.movie.rating)
        other_movie = Movie("other", 2001, 1.0)

        result = self.movie > other_movie
        expected = '"name" is better than "other"'

        self.assertEqual(expected, result)

    def test_movie_rating_lower_than_the_other_one(self):
        self.assertEqual(1.5, self.movie.rating)
        other_movie = Movie("other", 2001, 2.0)

        result = self.movie > other_movie
        expected = '"other" is better than "name"'

        self.assertEqual(expected, result)

    def test_repr(self):
        self.movie.add_actor("name1")
        self.movie.add_actor("name2")

        expected = """Name: name\nYear of Release: 2000\nRating: 1.50\nCast: name1, name2"""

        self.assertEqual(expected, repr(self.movie))

    def test_repr_empty_list_of_actors(self):
        self.assertEqual([], self.movie.actors)

        expected = """Name: name\nYear of Release: 2000\nRating: 1.50\nCast: """

        self.assertEqual(expected, repr(self.movie))


if __name__ == '__main__':
    main()
