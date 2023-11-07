from typing import List, Dict, Optional
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []   # store the users (users object) of the library
        self.books_available: Dict[str, List[str]] = {}   # {author: [books_available_name]}
        self.rented_books: Dict[str, Dict[str, int]] = {}  # {usernames: {book_names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available.keys():
            if book_name in self.books_available[author]:
                if user not in self.user_records:
                    self.user_records.append(user)
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books.keys():
                    self.rented_books[user.username] = {}
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for book in self.rented_books.values():
            if book_name in book.keys():
                days = book[book_name]
                return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User) -> Optional[str]:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        return f"{user.username} doesn't have this book in his/her records!"
