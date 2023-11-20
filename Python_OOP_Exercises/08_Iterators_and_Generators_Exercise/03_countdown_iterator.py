class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.current = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        number = self.current
        self.current -= 1
        return number


# test code:
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
