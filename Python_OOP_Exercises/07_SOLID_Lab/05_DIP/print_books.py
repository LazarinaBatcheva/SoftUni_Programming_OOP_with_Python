from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class ConcreteFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book


# test code
# b = Book("The Adventures of Sherlock Holmes")
# formatter_ = ConcreteFormatter()
# printer = Printer()
# formatted_b = printer.get_book(b, formatter_)
# print(formatted_b)
