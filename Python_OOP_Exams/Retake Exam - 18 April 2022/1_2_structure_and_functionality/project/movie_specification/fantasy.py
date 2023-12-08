from project.movie_specification.movie import Movie


class Fantasy(Movie):
    DEFAULT_AGE_REG = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = DEFAULT_AGE_REG):
        super().__init__(title, year, owner, age_restriction)

    @property
    def get_age_limit(self) -> int:
        return self.DEFAULT_AGE_REG
