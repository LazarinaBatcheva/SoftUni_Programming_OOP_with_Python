from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self):
        super().__init__(interest_rate=3.5, amount=50_000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
