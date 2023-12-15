from typing import Any

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVERS_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    @staticmethod
    def find_obj(searching_el, searching_attribute: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attribute) == searching_el), None)

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        if diver_type not in self.VALID_DIVERS_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = self.find_obj(diver_name, "name", self.divers)
        if diver is not None:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self.find_obj(fish_name, "name", self.fish_list)
        if fish is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        diver = self.find_obj(diver_name, "name", self.divers)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = self.find_obj(fish_name, "name", self.fish_list)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            elif not is_lucky:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self) -> str:
        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str) -> str:
        diver = self.find_obj(diver_name, "name", self.divers)

        result = [f"**{diver_name} Catch Report**"]
        fish_details = [f.fish_details() for f in diver.catch]
        result.extend(fish_details)

        return "\n".join(result)

    def competition_statistics(self) -> str:
        result = [f"**Nautical Catch Challenge Statistics**"]

        health_divers = [str(d) for d in sorted(self.divers, key=lambda d:
        (-d._competition_points, -len(d.catch), d.name)) if not d.has_health_issue]

        result.extend(health_divers)

        return "\n".join(result)
