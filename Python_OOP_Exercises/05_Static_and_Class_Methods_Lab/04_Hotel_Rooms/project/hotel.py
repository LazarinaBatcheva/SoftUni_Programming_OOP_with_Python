from typing import List

from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: Room, people: int):
        [room.take_room(people) for room in self.rooms if room.number == room_number]

    def free_room(self, room_number: Room):
        [room.free_room() for room in self.rooms if room.number == room_number]

    def status(self):
        free_rooms = []
        taken_rooms = []

        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
                self.guests += room.guests
            else:
                free_rooms.append(str(room.number))

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}")