from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    @property
    def get_service_type(self) -> str:
        return "Main Service"
