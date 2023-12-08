from typing import Any

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []

    @staticmethod
    def find_obj(looking_el, looking_attribute: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, looking_attribute) == looking_el), None)

    @staticmethod
    def check_for_movie_owner(user: User, movie: Movie):
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    @staticmethod
    def check_if_movie_uploaded(movie: Movie):
        if not movie.uploaded:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    def register_user(self, username: str, age: int) -> str:
        user = self.find_obj(username, "username", self.users_collection)
        if user is not None:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> str:
        user = self.find_obj(username, "username", self.users_collection)

        if user is None:
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        movie.uploaded = True
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> str:
        self.check_if_movie_uploaded(movie)     # if movie isn`t uploaded raises Exception

        user = self.find_obj(username, "username", self.users_collection)
        self.check_for_movie_owner(user, movie)

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> str:
        self.check_if_movie_uploaded(movie)     # if movie isn`t uploaded raises Exception

        user = self.find_obj(username, "username", self.users_collection)
        self.check_for_movie_owner(user, movie)     # if movie isn`t uploaded raises Exception

        # if not raised Exceptions movie deleted
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        movie.uploaded = False

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> str:
        user = self.find_obj(username, "username", self.users_collection)

        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> str:
        user = self.find_obj(username, "username", self.users_collection)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{username} disliked {movie.title} movie."

    def display_movies(self) -> str:
        if not self.movies_collection:
            return "No movies found."

        uploaded_movies = [m.details() for m in
                           sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))]

        return "\n".join(uploaded_movies)

    def __str__(self):
        usernames = [u.username for u in self.users_collection]
        movies_titles = [m.title for m in self.movies_collection]

        return (f"All users: {', '.join(usernames) if usernames else 'No users.'}\n"
                f"All movies: {', '.join(movies_titles) if movies_titles else 'No movies.'}")
