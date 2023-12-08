from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(5)

    def test_initialization(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_property_total_sold_books(self):
        bookstore = Bookstore(10)

        self.assertEqual(bookstore.total_sold_books, 0)

    def test_setter_books_limit_num_of_books_less_than_or_equal_to_0_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        expected = "Books limit of 0 is not valid"
        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -1
        expected = "Books limit of -1 is not valid"
        self.assertEqual(expected, str(ve.exception))

    def test_receive_book_books_in_store_plus_given_books_num_greater_than_books_limit_raises(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 3}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book3", 2)
        expected = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected, str(ex.exception))

    def test_receive_book_non_existing_book_added_new_book_returns_msg(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 1}

        result = self.bookstore.receive_book("book3", 2)
        expected = "2 copies of book3 are available in the bookstore."

        self.assertEqual(expected, result)

    def test_receive_book_existing_book_increase_book_count_returns_msg(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 1}

        result = self.bookstore.receive_book("book1", 2)
        expected = "3 copies of book1 are available in the bookstore."

        self.assertEqual(expected, result)

    def test_sell_book_non_existing_book_raises(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 2}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book3", 2)
        expected = "Book book3 doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_wanted_books_num_for_sell_more_than_book_count_raises(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 2, "book3": 1}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book1", 3)
        expected = "book1 has not enough copies to sell. Left: 1"
        self.assertEqual(expected, str(ex.exception))

    def test_sell_book_success_decrease_book_count_and_increase_total_sold_books_count_returns_msg(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 2, "book2": 3}

        result = self.bookstore.sell_book("book2", 2)
        expected = "Sold 2 copies of book2"

        self.assertEqual({"book1": 2, "book2": 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(expected, result)

    def test_len_bookstore_returns_total_count_of_books(self):
        self.bookstore.receive_book("book1", 1)
        self.bookstore.receive_book("book2", 3)

        result = len(self.bookstore)

        self.assertEqual(4, result)

    def test_len_empty_bookstore_returns_0(self):
        self.bookstore.availability_in_store_by_book_titles = {}

        result = len(self.bookstore)

        self.assertEqual(0, result)

    def test_str(self):
        self.bookstore.availability_in_store_by_book_titles = {"book1": 1, "book2": 2, "book3": 2}

        self.bookstore.sell_book("book1", 1)
        self.bookstore.sell_book("book2", 1)

        expected = """Total sold books: 2
Current availability: 3
 - book1: 0 copies
 - book2: 1 copies
 - book3: 2 copies"""
        result = str(self.bookstore)

        self.assertEqual({"book1": 0, "book2": 1, "book3": 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
