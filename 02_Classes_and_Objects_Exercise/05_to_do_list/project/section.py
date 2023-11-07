from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task):
        for show in self.tasks:
            if new_task.name == show.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for t_name in self.tasks:
            if task_name == t_name.name:
                t_name.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(self.tasks):
            if tasks.completed:
                count += 1
                self.tasks.remove(tasks)
        return f"Cleared {count} tasks."

    def view_section(self):
        return f"Section {self.name}:" + "\n" + "\n".join(task_.details() for task_ in self.tasks)
