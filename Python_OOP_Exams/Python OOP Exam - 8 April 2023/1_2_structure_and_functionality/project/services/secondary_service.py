from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    @property
    def get_service_type(self) -> str:
        return "Secondary Service"
