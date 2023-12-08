from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes: int = 0
        self.uploaded: bool = False

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title.strip() == "":
            raise ValueError("The title cannot be empty string!")
        self.__title = title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = year

    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = owner

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, age_restriction):
        age_limit = self.get_age_limit
        if age_restriction < age_limit:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted "
                             f"for audience under {age_limit} years!")
        self.__age_restriction = age_restriction

    @property
    @abstractmethod
    def get_age_limit(self):
        pass

    def details(self) -> str:
        return (f"{self.__class__.__name__} - Title:{self.title}, "
                f"Year:{self.year}, "
                f"Age restriction:{self.age_restriction}, "
                f"Likes:{self.likes}, "
                f"Owned by:{self.owner.username}")
