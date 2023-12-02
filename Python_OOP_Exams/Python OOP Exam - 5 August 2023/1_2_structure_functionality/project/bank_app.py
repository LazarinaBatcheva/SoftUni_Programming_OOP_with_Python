from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOANS_VALID_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENTS_VALID_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def find_loan_by_type(self, loan_type: str):
        return next((loan for loan in self.loans if loan.__class__.__name__ == loan_type), None)

    def find_client_by_id(self, client_id: str):
        return next((c for c in self.clients if c.client_id == client_id), None)

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.LOANS_VALID_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.LOANS_VALID_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self.CLIENTS_VALID_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        client = self.CLIENTS_VALID_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self.find_loan_by_type(loan_type)
        client = self.find_client_by_id(client_id)

        if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or \
                (loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"):
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = len([c.increase_clients_interest() for c in self.clients
                                           if c.interest < min_rate])

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(sum(loan.amount for loan in c.loans) for c in self. clients)
        not_granted_sum = sum(loan.amount for loan in self.loans)

        try:
            avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        result = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {total_clients_income:.2f}",
            f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
                  ]

        return "\n".join(result)
