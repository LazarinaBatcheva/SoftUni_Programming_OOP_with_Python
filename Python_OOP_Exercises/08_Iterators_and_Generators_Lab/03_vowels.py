class vowels:
    def __init__(self, string: str):
        self.string = string
        searched_vowels = "aeiouy"
        self.found_vowels = [ch for ch in self.string if ch.lower() in searched_vowels]
        self.current_index = 0
        self.end_index = len(self.found_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration
        index = self.current_index
        self.current_index += 1
        return self.found_vowels[index]


# test code
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
