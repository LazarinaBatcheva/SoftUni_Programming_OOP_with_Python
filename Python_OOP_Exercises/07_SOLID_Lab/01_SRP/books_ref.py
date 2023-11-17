from typing import List, Optional


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'Book "{self.title}" by {self.author} with {self.page} pages'


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str) -> Optional[list[Book]]:
        try:
            book = [b for b in self.books if b.title.lower() == title]
            return book
        except IndexError:
            return None


# test code
book1 = Book("Book1", "Author1")
book2 = Book("Book2", "Author2")
library = Library()
print(library.books)
library.add_book(book1)
print(library.books)
library.add_book(book2)
print(library.books)
book1.turn_page(50)
book2.turn_page(100)
print(library.find_book("Book3"))
print(library.find_book("book1"))
print(library.find_book("book2"))