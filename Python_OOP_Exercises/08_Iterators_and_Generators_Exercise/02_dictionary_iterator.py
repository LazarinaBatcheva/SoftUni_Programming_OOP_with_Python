class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj
        self.items_iter = iter(self.obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.items_iter)


# test code:
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print()
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
