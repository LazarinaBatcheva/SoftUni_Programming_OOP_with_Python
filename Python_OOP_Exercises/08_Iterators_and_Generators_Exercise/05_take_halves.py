def solution():

    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        return [item for item, _ in zip(seq, range(n))]

    return (take, halves, integers)


# test code
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
print()
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
