from typing import Any

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: list[Hardware] = []
    _software: list[Software] = []

    # HELPERS
    @staticmethod
    def __find_obj(searching_el, searching_attr: str, collection: list) -> Any:
        return next((obj for obj in collection if getattr(obj, searching_attr) == searching_el), None)

    # LOGIC
    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int) -> None:
        hardware = System.__find_obj(name, "name", System._hardware)

        if hardware is not None:
            return

        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = System.__find_obj(name, "name", System._hardware)

        if hardware is not None:
            return

        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        hardware = System.__find_obj(hardware_name, "name", System._hardware)

        if hardware is None:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int) -> Any:
        hardware = System.__find_obj(hardware_name, "name", System._hardware)

        if hardware is None:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> Any:
        hardware = System.__find_obj(hardware_name, "name", System._hardware)
        software = System.__find_obj(software_name, "name", System._software)

        if hardware is None or software is None:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze() -> str:
        total_software_memory = sum(s.memory_consumption for s in System._software)
        total_hardware_memory = sum(h.memory for h in System._hardware) + total_software_memory
        total_software_capacity = sum(s.capacity_consumption for s in System._software)
        total_hardware_capacity = sum(h.capacity for h in System._hardware) + total_software_capacity

        return (f"System Analysis\n"
                f"Hardware Components: {len(System._hardware)}\n"
                f"Software Components: {len(System._software)}\n"
                f"Total Operational Memory: {total_software_memory} / {total_hardware_memory}\n"
                f"Total Capacity Taken: {total_software_capacity} / {total_hardware_capacity}")

    @staticmethod
    def system_split() -> str:
        result = [str(h) for h in System._hardware]

        return "\n".join(result)
