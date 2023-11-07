from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("Element isn`t a string, please add only a string")
        self.data.append(element)

    def pop(self) -> str:
        last_element = self.data.pop()
        return last_element

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f"[{', '.join(reversed_data)}]"
