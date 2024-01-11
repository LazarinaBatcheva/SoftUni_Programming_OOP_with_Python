from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: list[BaseDecoration] = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        return next((d for d in self.decorations if d.decoration_type == decoration_type), "None")
