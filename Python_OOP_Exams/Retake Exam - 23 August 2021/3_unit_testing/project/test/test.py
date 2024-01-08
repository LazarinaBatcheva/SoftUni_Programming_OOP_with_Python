from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("name")

    def test_initialization(self):
        self.assertEqual("name", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_setter_name_empty_string_raises(self):
        self.assertEqual("name", self.library.name)

        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_book_empty_booking_dict_success(self):
        self.assertEqual({}, self.library.books_by_authors)

        self.library.add_book("author", "title")

        self.assertEqual({"author": ["title"]}, self.library.books_by_authors)

    def test_add_book_existing_author_non_existing_book_success(self):
        self.library.books_by_authors = {"author": ["book1"]}

        self.library.add_book("author", "book2")

        self.assertEqual({"author": ["book1", "book2"]}, self.library.books_by_authors)

    def test_add_book_non_existing_author_success(self):
        self.library.books_by_authors = {"author": ["book1"]}

        self.library.add_book("another author", "book1")

        self.assertEqual({"author": ["book1"], "another author": ["book1"]}, self.library.books_by_authors)

    def test_add_book_existing_author_existing_book_failure(self):
        self.library.books_by_authors = {"author": ["book1", "book2"]}

        self.library.add_book("author", "book1")

        self.assertEqual({"author": ["book1", "book2"]}, self.library.books_by_authors)

    def test_add_reader_empty_readers_dict_success(self):
        self.assertEqual({}, self.library.readers)

        self.library.add_reader("reader")

        self.assertEqual({"reader": []}, self.library.readers)

    def test_add_reader_existing_reader_failure(self):
        self.library.readers = {"reader": []}

        result = self.library.add_reader("reader")
        expected = "reader is already registered in the name library."

        self.assertEqual({"reader": []}, self.library.readers)
        self.assertEqual(expected, result)

    def test_rent_book_non_existing_reader_failure(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader("reader")

        result = self.library.rent_book("someone else", "author", "title")
        expected = "someone else is not registered in the name Library."

        self.assertEqual({"reader": []}, self.library.readers)
        self.assertEqual(expected, result)

    def test_rent_book_non_existing_author_failure(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

        self.library.add_book("author", "book1")
        self.library.add_reader("reader")

        result = self.library.rent_book("reader", "other author", "title")
        expected = "name Library does not have any other author's books."

        self.assertEqual({"author": ["book1"]}, self.library.books_by_authors)
        self.assertEqual({"reader": []}, self.library.readers)
        self.assertEqual(expected, result)

    def test_rent_book_non_existing_book_failure(self):
        self.library.books_by_authors = {"author": ["book1"]}
        self.library.readers = {"reader": []}

        result = self.library.rent_book("reader", "author", "some book")
        expected = """name Library does not have author's "some book"."""

        self.assertEqual({"reader": []}, self.library.readers)
        self.assertEqual(expected, result)

    def test_rent_book_success_readers_dict_add_book_books_dict_remove_book(self):
        self.library.books_by_authors = {"author": ["book1", "book2"]}
        self.library.readers = {"reader": []}

        self.library.rent_book("reader", "author", "book1")

        self.assertEqual({"reader": [{"author": "book1"}]}, self.library.readers)
        self.assertEqual({"author": ["book2"]}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
