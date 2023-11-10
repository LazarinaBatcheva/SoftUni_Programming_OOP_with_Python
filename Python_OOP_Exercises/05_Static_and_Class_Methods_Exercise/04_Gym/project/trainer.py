class Trainer:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.id
        Trainer.id += 1

    @staticmethod
    def get_next_id() -> int:
        return Trainer.id

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
