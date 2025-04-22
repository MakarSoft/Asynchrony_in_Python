# fishing.py
# ----------

import heapq
import random
import time

from typing import Optional, List


class Fisherman:

    def __init__(
        self,
        name: str = "Рыбак",
        number_of_rods: int = 9
    ) -> None:
        self.name = name
        self.number_of_rods = number_of_rods
        self.total_caught = 0
        self._rod_heap: List[tuple[float, int, int]] = []

    def start_fishing(
        self,
        number_of_rods: Optional[int] = None
    ) -> None:
        """
        Запускает процесс рыбалки
        """

        self.total_caught = 0
        self._rod_heap = []

        number_of_rods = (
            min(number_of_rods, self.number_of_rods)
            if number_of_rods
            else self.number_of_rods
        )

        # Инициализация удочек с разным временем ожидания
        # ...закидываем удочки ))
        for rod_number in range(1, self.number_of_rods + 1):
            waiting = random.randint(1, 10)
            heapq.heappush(
                self._rod_heap,
                (
                    time.perf_counter() + waiting,
                    rod_number,
                    waiting
                )
            )

    def fishing_loop(
        self
    ) -> None:

        while self._rod_heap:
            current_time = time.perf_counter()
            trigger_time, rod_number, wait_time = heapq.heappop(self._rod_heap)

            if current_time < trigger_time:
                # Ждем до момента срабатывания с точностью 0.1 сек
                time.sleep(max(0.0, trigger_time - current_time))

            # Ловим рыбу
            self.total_caught += 1
            # ! временно отключаем
            # print(
            #     f"{self.name} поймал одну, всего {self.total_caught}"
            #     f"\n\tНа удочке №{rod_number} после {wait_time} сек. ожидания"
            # )

def main(number_of_rods: int = 9):
    fisherman = Fisherman("Борщов", number_of_rods)
    fisherman.start_fishing()
    fisherman.fishing_loop()


# ----------------------------------------------------------
if __name__ == "__main__":

    print("Рыбалка без использования потоков и asyncio")
    for number_of_rods in (10,100,1000,10000, 100000):
        start_time = time.perf_counter()
        main(number_of_rods)
        print(
            f"Число удочек: {number_of_rods}, "
            f"Общее время: {time.perf_counter() - start_time:.2f} сек."
        )
