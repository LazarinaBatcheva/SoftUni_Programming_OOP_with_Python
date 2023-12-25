from typing import Any

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    __VALID_SUSTENANCE_TYPES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *players: Player) -> str:
        players_names = []  # names of the new added players
        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_names.append(player.name)

        return f"Successfully added: {', '.join(players_names)}"

    def add_supply(self, *supplies: Supply) -> None:
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.__VALID_SUSTENANCE_TYPES:
            return

        player = self.__find_obj(player_name, "name", self.players)

        if player is None:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supply = self.__get_last_supply(sustenance_type)

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        # Increase player`s stamina with supply`s energy
        self.__increase_players_stamina(player, supply)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_player = self.__find_obj(first_player_name, "name", self.players)
        second_player = self.__find_obj(second_player_name, "name", self.players)

        # Check if duel is possible
        msg = ""
        if first_player.stamina == 0:
            msg += f"Player {first_player_name} does not have enough stamina.\n"
        if second_player.stamina == 0:
            msg += f"Player {second_player_name} does not have enough stamina."
        if msg:
            return msg.strip()

        # Determine of attacker and defender and implementation of a duel
        if first_player < second_player:
            result = self.__duel(first_player, second_player)
        else:
            result = self.__duel(second_player, first_player)

        return result

    def next_day(self) -> None:
        for player in self.players:
            reduce_value = player.age * 2
            if player.stamina - reduce_value < 0:
                player.stamina = 0
            else:
                player.stamina -= reduce_value

            # Increase player`s stamina
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []

        players_info = [str(p) for p in self.players]
        supplies_info = [s.details() for s in self.supplies]

        result.extend(players_info)
        result.extend(supplies_info)

        return "\n".join(result)

    # HELPERS
    @staticmethod
    def __find_obj(searching_el, attribute_el, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, attribute_el) == searching_el), None)

    @staticmethod
    def __increase_players_stamina(player, supply) -> None:
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy

    @staticmethod
    def __duel(first_p, second_p):
        if second_p.stamina - (first_p.stamina / 2) <= 0:
            second_p.stamina = 0
            return f"Winner: {first_p.name}"
        second_p.stamina -= (first_p.stamina / 2)

        if first_p.stamina - (second_p.stamina / 2) <= 0:
            first_p.stamina = 0
            return f"Winner: {second_p.name}"
        first_p.stamina -= (second_p.stamina / 2)

        winner = second_p.name if first_p < second_p else first_p.name
        return f"Winner: {winner}"

    def __get_last_supply(self, sustenance_type: str) -> Any:
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].get_supply_type == sustenance_type:
                return self.supplies.pop(i)
