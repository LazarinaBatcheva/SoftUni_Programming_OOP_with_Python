def squares(number: int):
    for num in range(1, number + 1):
        yield num ** 2


# test code
print(list(squares(5)))