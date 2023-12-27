from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    @property
    def strength_comparison_value(self) -> int:
        return 100

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak.name)
