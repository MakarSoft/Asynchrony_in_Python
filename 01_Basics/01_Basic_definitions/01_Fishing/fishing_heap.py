import heapq
import random

from time import perf_counter, sleep
from typing import List


class Fisherman:
    """
    Рыбак
    """

    def __init__(
        self, name: str = "Рыбак",
        number_of_fishing_rods: int = 9
    ) -> None:
        self.name = name
        self.number_of_fishing_rods = number_of_fishing_rods    # число удочек
        self.total_caught = 0   # число пойманных рыб

    def start_fishing(self) -> None:
        """
        Запускает процесс рыбалки
        используем кучу(heap) для оптимизации
        """

        self.total_caught = 0
        heap: List[tuple[float, int, int]] = []

        # Инициализация удочек с разным временем ожидания
        # ...закидываем удочки ))
        for rod_number in range(1, self.number_of_fishing_rods + 1):
            waiting_time = random.randint(1, 10)
            heapq.heappush(
                heap,
                (
                    perf_counter() + waiting_time,
                    rod_number,
                    waiting_time
                )
            )

        while heap:
            current_time = perf_counter()
            trigger_time, rod_number, wait_time = heapq.heappop(heap)

            if current_time < trigger_time:
                # Ждем до момента срабатывания с точностью 0.1 сек
                sleep(max(0.0, trigger_time - current_time))

            # Ловим рыбу
            self.total_caught += 1
            print(f"{self.name} поймал одну, всего {self.total_caught}")
            print(f"\tНа удочке №{rod_number} после {wait_time} сек. ожидания")


if __name__ == "__main__":

    start_time = perf_counter()
    fisherman = Fisherman("Борщов", 9)
    fisherman.start_fishing()
    print(f"Общее время: {perf_counter() - start_time:.2f} сек.")
