# deque_test_01.py
# Тестирование скорости работы deque и list

import time
from collections import deque
from random import randint


SIZE = 1000000

lst = [randint(1, 1000) for _ in range(SIZE)]
dq = deque(lst)

# тестирование скорости работы list
start = time.perf_counter()
for _ in range(SIZE):
    lst.pop(0)
end = time.perf_counter()
print(f"list: {end - start}")

# тестирование скорости работы deque и list
start = time.perf_counter()
for _ in range(SIZE):
    dq.popleft()
end = time.perf_counter()
print(f"deque: {end - start}")

# SIZE = 1000000
# deque: 0.10360874596517533
# list: 737.1650670029921       ???!!!

# SIZE = 100000
# deque: 0.00968888693023473
# list: 3.4193049060413614
