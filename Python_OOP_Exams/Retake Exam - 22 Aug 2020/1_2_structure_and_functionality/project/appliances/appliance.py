from abc import ABC


class Appliance(ABC):
    def __init__(self, cost: float):
        self.cost = cost    # The cost is for a single day

    def get_monthly_expense(self) -> float:
        # Return the cost for a month (30 days)
        return self.cost * 30
