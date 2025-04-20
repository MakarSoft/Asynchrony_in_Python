# упрощенной версии с тремя элементами без рандома.

from time import time, sleep, perf_counter
from itertools import count
import heapq


total_count = count(1)


class FishingRod:
    def __init__(self, delay: float | int, name: str = ""):
        self.name = name
        self.delay = delay

    def get(self):
        if self.delay > 0:
            return True, self.delay
        print(f"На удочку №{self.name} поймал одну, всего {next(total_count)}")
        return False, None


def main():
    tasks = []
    for i in (2, 5, 4):
        delay = i
        tasks.append((time() + delay, i, FishingRod(delay=delay, name=str(i))))
    heapq.heapify(tasks)

    while tasks:
        time_mark, _id, fishing_rod = heapq.heappop(tasks)
        wait_time = time_mark - time()
        if wait_time > 0:
            print(f"{wait_time=}")
            sleep(wait_time)

        state, delay = fishing_rod.get()
        fishing_rod.delay -= time() - time_mark
        if state:
            heapq.heappush(tasks, (time() - time_mark, _id, fishing_rod))


start_time = perf_counter()
main()
print(perf_counter() - start_time)
