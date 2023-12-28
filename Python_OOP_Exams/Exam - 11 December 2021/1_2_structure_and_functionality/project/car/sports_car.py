from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600

    @property
    def get_min_speed_limit(self) -> int:
        return self.MIN_SPEED_LIMIT

    @property
    def get_max_speed_limit(self) -> int:
        return self.MAX_SPEED_LIMIT
