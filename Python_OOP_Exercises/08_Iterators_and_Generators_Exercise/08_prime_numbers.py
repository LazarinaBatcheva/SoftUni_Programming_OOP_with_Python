from math import sqrt
from typing import List


def get_primes(numbers: List[int]):
    return (n for n in numbers if n > 1 and all(n % i != 0 for i in range(2, int(sqrt(n)) + 1)))


# test code
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print()
print(list(get_primes([-2, 0, 0, 1, 1, 0])))