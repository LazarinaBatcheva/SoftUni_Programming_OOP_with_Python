from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: list[Room] = []

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        total_consumption = sum(room.expenses + room.room_cost for room in self.rooms)

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self) -> str:
        result = []

        for room in self.rooms:
            expenses = room.expenses + room.room_cost
            if room.budget < expenses:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
            else:
                room.budget -= expenses
                result.append(f"{room.family_name} paid {expenses:.2f}$ "
                              f"and have {room.budget:.2f}$ left.")

            return "\n".join(result)

    def status(self) -> str:
        result = [f"Total population: {sum(room.members_count for room in self.rooms)}"]
        [result.append(str(room)) for room in self.rooms]

        return "\n".join(result)
