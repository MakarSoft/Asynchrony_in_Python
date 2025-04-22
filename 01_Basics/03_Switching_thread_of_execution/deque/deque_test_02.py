# deque_test_02.py
# Тестирование скорости работы deque и list

from collections import deque
from random import randint
from time import perf_counter


SIZE = 100000


def pop1(lst: list) -> None:
    ''' list.pop(0) - очень медленно O(n) '''

    size = len(lst)
    for _ in range(size):
        val = lst.pop(0)
        lst.append(val)


def pop2(lst: deque) -> None:
    ''' deque.popleft() - очень быстро O(1) '''

    size = len(lst)
    for _ in range(size):
        val = lst.popleft()
        lst.append(val)


if __name__ == "__main__":
    for func, t in ((pop1, list), (pop2, deque)):

        # наплнение тестируемой структуры t
        # данными (последовательность чисел)...

        data = t(randint(1, 1000) for _ in range(SIZE))
        # или просто
        # data = t(range(SIZE))

        # ...и замер времени
        start = perf_counter()
        func(data)
        end = perf_counter()

        print(f"{t.__name__}: {end - start}")

# list: 4.210399529983988
# deque: 0.00797307799803093
