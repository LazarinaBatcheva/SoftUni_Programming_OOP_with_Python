from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        if not 51 <= table_number <= 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        super().__init__(table_number, capacity)
        self.__table_number = table_number
