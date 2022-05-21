"""
First lecture iterators
"""


class SquareSecuence:
    """Return square sequence"""

    def __init__(self, length):
        self.counter = 0
        self.length = length

    def __len__(self):
        return self.length

    def __next__(self):
        if self.counter > self.length:
            raise StopIteration

        rezult = self.counter**2
        self.counter += 1

        return rezult

    def __iter__(self):
        return self


sq = SquareSecuence(64)

for i in enumerate(sq):
    print(i)
