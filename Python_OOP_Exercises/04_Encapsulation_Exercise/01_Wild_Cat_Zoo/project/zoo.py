from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        needed_money_for_workers = sum(worker.salary for worker in self.workers)
        if self.__budget >= needed_money_for_workers:
            self.__budget -= needed_money_for_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        needed_money_for_animals = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= needed_money_for_animals:
            self.__budget -= needed_money_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            else:
                cheetahs.append(repr(animal))

        animals_info = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        animals_info.extend(lions)
        animals_info.append(f"----- {len(tigers)} Tigers:")
        animals_info.extend(tigers)
        animals_info.append(f"----- {len(cheetahs)} Cheetahs:")
        animals_info.extend(cheetahs)

        return "\n".join(animals_info)

    def workers_status(self) -> str:
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            else:
                vets.append(repr(worker))

        worker_infos = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        worker_infos.extend(keepers)
        worker_infos.append(f"----- {len(caretakers)} Caretakers:")
        worker_infos.extend(caretakers)
        worker_infos.append(f"----- {len(vets)} Vets:")
        worker_infos.extend(vets)

        return "\n".join(worker_infos)

