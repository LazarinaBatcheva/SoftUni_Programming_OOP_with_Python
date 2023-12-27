from typing import List, Any

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        if climber_type not in self.VALID_CLIMBERS_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = self.__find_obj(climber_name, "name", self.climbers)

        if climber is not None:
            return f"{climber_name} has been already registered."

        new_climber = self.VALID_CLIMBERS_TYPES[climber_type](climber_name)
        self.climbers.append(new_climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        if peak_type not in self.VALID_PEAKS_TYPES:
            return f"{peak_type} is an unknown type of peak."

        peak = self.VALID_PEAKS_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]) -> str:
        climber = self.__find_obj(climber_name, "name", self.climbers)
        peak = self.__find_obj(peak_name, "name", self.peaks)

        missing_equipment = []
        for el in peak.get_recommended_gear():
            if el not in gear:
                missing_equipment.append(el)
        if missing_equipment:
            climber.is_prepared = False
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(sorted(missing_equipment))}.")

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        climber = self.__find_obj(climber_name, "name", self.climbers)
        if climber is None:
            return f"Climber {climber_name} is not registered yet."

        peak = self.__find_obj(peak_name, "name", self.peaks)
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        successful_climbers = []
        conquered_peaks_set = set()
        for climber in self.climbers:
            if climber.conquered_peaks:
                successful_climbers.append(climber)
                for peak in climber.conquered_peaks:
                    conquered_peaks_set.add(peak)

        sorted_climbers = sorted(successful_climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        result = [f"Total climbed peaks: {len(conquered_peaks_set)}\n**Climber's statistics:**"]
        climbers_info = [str(c) for c in sorted_climbers]
        result.extend(climbers_info)

        return "\n".join(result)

    # HELPERS
    @staticmethod
    def __find_obj(searching_el, searching_attr: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attr) == searching_el), None)
