from itertools import permutations


def possible_permutations(numbers: list):
    for perm in permutations(numbers):
        yield list(perm)


# test code
[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]