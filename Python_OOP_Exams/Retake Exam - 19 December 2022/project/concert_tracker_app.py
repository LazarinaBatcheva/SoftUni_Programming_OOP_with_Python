from typing import List, Any

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer
                            }
    SKILLS_REQUIRED = {
        "Rock": {"Drummer": ["play the drums with drumsticks"],
                 "Singer": ["sing high pitch notes"],
                 "Guitarist": ["play rock"]},
        "Metal": {"Drummer": ["play the drums with drumsticks"],
                  "Singer": ["sing low pitch notes"],
                  "Guitarist": ["play metal"]},
        "Jazz": {"Drummer": ["play the drums with drum brushes"],
                 "Singer": ["sing high pitch notes",
                            "sing low pitch notes"],
                 "Guitarist": ["play jazz"]}
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @staticmethod
    def find_object(looking_name, name_attribute: str, collection: list) -> Any:
        for obj in collection:
            if getattr(obj, name_attribute) == looking_name:
                return obj

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = self.find_object(name, "name", self.musicians)

        if musician is not None:
            raise Exception(f"{name} is already a musician!")

        new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        band = self.find_object(name, "name", self.bands)

        if band is not None:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        concert = self.find_object(place, "place", self.concerts)

        if concert is not None:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        musician = self.find_object(musician_name, "name", self.musicians)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.find_object(band_name, "name", self.bands)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        band = self.find_object(band_name, "name", self.bands)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.find_object(musician_name, "name", band.members)

        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        band = self.find_object(band_name, "name", self.bands)
        concert = self.find_object(concert_place, "place", self.concerts)

        member_types = [m.__class__.__name__ for m in band.members]
        members = {"Singer": 0, "Drummer": 0, "Guitarist": 0}
        for member_type in member_types:
            if member_type in members.keys():
                members[member_type] += 1
        if any(member == 0 for member in members.values()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for member in band.members:
            member_type = member.__class__.__name__
            required_skills = self.SKILLS_REQUIRED[concert.genre][member_type]
            if not all(skill in member.skills for skill in required_skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.calculate_profit()

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
