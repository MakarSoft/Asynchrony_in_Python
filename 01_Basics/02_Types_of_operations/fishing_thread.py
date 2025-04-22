# fishing_thread.py
# ------------------

import random
import time

from concurrent.futures import ThreadPoolExecutor
from typing import Optional


class Fisherman:

    def __init__(
        self,
        name: str = "Рыбак",
        number_of_rods: int = 9
    ) -> None:
        self.name = name
        self.number_of_rods = number_of_rods  # Количество удочек
        self.total_caught = 0  # Общее количество пойманных рыб

    def fish(
        self,
        rod_number: int,    # Номер удочки
        wait_time: int      # Время ожидания
    ) -> None:
        """Задача для ловли рыбы."""

        time.sleep(wait_time)
        self.total_caught += 1
        # ! временно отключаем для теста производительности...
        # print(
        #     f"{self.name} поймал одну рыбу"
        #     f"\n\tна удочке №{rod_number} после {wait_time} сек. ожидания."
        #     f"\n\tВсего поймано {self.total_caught} рыб"
        # )

    def start_fishing(
        self,
        number_of_rods: Optional[int] = None    # Количество удочек
    ) -> None:
        """
        Запускает процесс рыбалки
        """

        self.total_caught = 0

        number_of_rods = (
            min(number_of_rods, self.number_of_rods)
            if number_of_rods
            else self.number_of_rods
        )

        with ThreadPoolExecutor(max_workers=number_of_rods) as executer:
            for rod_num in range(1, number_of_rods+1):
                waiting = random.randint(1, 10)
                executer.submit(self.fish, rod_num, waiting)


def main(number_of_rods: int = 9):
    fisherman = Fisherman("Борщов", number_of_rods)
    fisherman.start_fishing()


# ----------------------------------------------------------
if __name__ == "__main__":

    print("Рыбалка с использованием потоков")
    for number_of_rods in (10, 100, 1000, 10000, 100000):
        start_time = time.perf_counter()
        main(number_of_rods)
        print(
            f"Число удочек: {number_of_rods}, "
            f"Общее время: {time.perf_counter() - start_time:.2f} сек."
        )


# Число удочек: 10, Общее время: 10.00 сек.
# Число удочек: 100, Общее время: 10.10 сек.
# Число удочек: 1000, Общее время: 10.29 сек.
# Число удочек: 10000, Общее время: 13.97 сек.
# Число удочек: 100000, Общее время: 73.62 сек.
