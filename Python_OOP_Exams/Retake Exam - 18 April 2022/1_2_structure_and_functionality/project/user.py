class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list = []
        self.movies_owned: list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if username.strip() == "":
            raise ValueError("Invalid username!")
        self.__username = username

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = age

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]

        if not self.movies_liked:
            result.append("No movies liked.")
        else:
            liked_movies = [m.details() for m in self.movies_liked]
            result.extend(liked_movies)
        result.append("Owned movies:")

        if not self.movies_owned:
            result.append("No movies owned.")
        else:
            owned_movies = [m.details() for m in self.movies_owned]
            result.extend(owned_movies)

        return "\n".join(result)
