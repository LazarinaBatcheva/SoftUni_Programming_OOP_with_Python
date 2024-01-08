from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        if not 1 <= table_number <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        super().__init__(table_number, capacity)
        self.__table_number = table_number
