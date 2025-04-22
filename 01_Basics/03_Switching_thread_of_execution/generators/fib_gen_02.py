from typing import Iterator


class Fibonacci:
    def __init__(self, num_elements: int = 0) -> None:
        if num_elements < 0:
            raise ValueError("Number of elements must be non-negative")
        self.num_elements = num_elements
        self._index = 0
        self._prev = 0
        self._current = 1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.num_elements > 0 and self._index >= self.num_elements:
            raise StopIteration

        if self._index == 0:
            result = self._prev
        elif self._index == 1:
            result = self._current
        else:
            self._prev, self._current = self._current, self._prev + self._current
            result = self._current

        self._index += 1
        return result


# Первые 5 чисел Фибоначчи
fib = Fibonacci(10)
print(list(fib))  # [0, 1, 1, 2, 3]

# Бесконечная последовательность (первые 6 элементов)
fib_infinite = Fibonacci()
for _ in range(10):
    print(next(fib_infinite), end=" ")  # 0 1 1 2 3 5
