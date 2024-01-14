from abc import ABC
from typing import Any

from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: list[Software] = []

    def install(self, software: Software) -> Any:
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.capacity -= software.capacity_consumption
        self.memory -= software.memory_consumption

    def uninstall(self, software: Software) -> None:
        self.software_components.remove(software)
        self.capacity += software.capacity_consumption
        self.memory += software.memory_consumption

    def __str__(self):
        express_software_count = len([s for s in self.software_components if s.software_type == "Express"])
        light_software_count = len([s for s in self.software_components if s.software_type == "Light"])

        total_software_memory = sum(s.memory_consumption for s in self.software_components)
        total_software_capacity = sum(s.capacity_consumption for s in self.software_components)

        return f"""Hardware Component - {self.name}
Express Software Components: {express_software_count}
Light Software Components: {light_software_count}
Memory Usage: {total_software_memory} / {total_software_memory + self.memory}
Capacity Usage: {total_software_capacity} / {total_software_capacity + self.capacity}
Type: {self.hardware_type}
Software Components: {', '.join(s.name for s in self.software_components) if self.software_components else 'None'}"""
