from collections import namedtuple
from typing import Self, Iterator


class Fibonacci:

    FibonacciPair = namedtuple("pair", ["prev", "last"])

    def __init__(self, num_elements: int = 0) -> None:
        if num_elements < 0:
            raise ValueError("Number of elements must be non-negative")

        self.num_elements = num_elements
        self._index = 0
        self._pair = self.FibonacciPair(0, 1)

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.num_elements > 0 and self._index >= self.num_elements:
            raise StopIteration

        if self._index < 2:
            result = self._pair[self._index]
        else:
            result = self._pair.prev + self._pair.last
            self._pair = self.FibonacciPair(self._pair.last, result)

        self._index += 1
        return result

# ==========================================================
if __name__ == "__main__":

    finite_gen = Fibonacci(0)
    i = 0
    for number in finite_gen:
        i += 1
        print(f"{i} -> {number}")
        if number > 100000000000000000000:
            break
    print("-" * 20)
