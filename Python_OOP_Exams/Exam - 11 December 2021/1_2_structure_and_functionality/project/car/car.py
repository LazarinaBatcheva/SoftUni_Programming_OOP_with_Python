from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")
        self.__model = model

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        min_speed_limit = self.get_min_speed_limit
        max_speed_limit = self.get_max_speed_limit

        if not min_speed_limit <= speed_limit <= max_speed_limit:
            raise ValueError(f"Invalid speed limit! Must be between {min_speed_limit} and {max_speed_limit}!")
        self.__speed_limit = speed_limit

    @property
    @abstractmethod
    def get_min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def get_max_speed_limit(self):
        pass
