from time import sleep, perf_counter
from itertools import count
from random import randrange
from typing import Optional, Union
import heapq


total_count = count(1)


class FishingRod:
    def __init__(self, delay: Union[float, int], name: str = ""):
        self.name = name
        self.delay = delay

    def get(self) -> tuple[bool, Optional[Union[float, int]]]:
        if self.delay > 0:
            return True, self.delay
        print(f"На удочку №{self.name} поймал одну, всего {next(total_count)}")
        return False, None


def main():
    n = 9
    tasks = []

    # инициируем удочки
    for i in range(1, n+1):
        delay = randrange(1, 11)
        tasks.append(
            (
                perf_counter() + delay,
                i,
                FishingRod(delay=delay, name=str(i))
            )
        )

    # формируем кучу из списка задач,
    # чтобы затем всегда брать самую приоритетную удочку
    heapq.heapify(tasks)

    while tasks:
        # берем задачу, получаем самую приоритетную
        time_mark, _id, fishing_rod = heapq.heappop(tasks)

        # считаем время необходимого ожидания
        wait_time = time_mark - perf_counter()
        if wait_time > 0:
            sleep(wait_time)
        state, delay = fishing_rod.get()  # смотрим на удочку, проверяем ее

        # обновляем время ожидания, отнимаем уже потраченное
        fishing_rod.delay = perf_counter() - time_mark

        # откладываем задачу обратно в список задач,
        # если время еще не пришло, клева пока нет.
        if state:
            heapq.heappush(
                tasks,
                (
                    perf_counter() - time_mark,
                    _id,
                    fishing_rod
                )
            )


start_time = perf_counter()
main()
print(perf_counter() - start_time)
