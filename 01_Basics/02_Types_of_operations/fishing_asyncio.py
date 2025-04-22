# fishing_asyncio.py
# ------------------

import asyncio
import random
import time

from typing import Optional

class Fisherman:

    def __init__(
        self,
        name: str = "Рыбак",    # Имя рыбака
        number_of_rods: int = 9 # Количество удочек
    ) -> None:
        self.name = name
        self.number_of_rods = number_of_rods
        self.total_caught = 0

    async def fish(
        self,
        rod_number: int,
        wait_time: int
    ) -> None:
        """Асинхронная задача для ловли рыбы."""

        await asyncio.sleep(wait_time)
        self.total_caught += 1
        # ! временно отключаем для теста производительности...
        # print(
        #     f"{self.name} поймал одну, всего {self.total_caught}"
        #     f"\n\tНа удочке №{rod_number} после {wait_time} сек. ожидания"
        # )

    async def start_fishing(
        self,
        number_of_rods: Optional[int] = None
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

        tasks = [
            self.fish(rod_num, random.randint(1, 10))
            for rod_num in range(1, number_of_rods)
        ]
        await asyncio.gather(*tasks)

async def main(number_of_rods: int = 9):
    fisherman = Fisherman("Борщов", number_of_rods)
    await fisherman.start_fishing()


# ----------------------------------------------------------
if __name__ == "__main__":

    print("Рыбалка с использованием asyncio")
    for number_of_rods in (10,100,1000,10000, 100000):
        start_time = time.perf_counter()
        asyncio.run(main(number_of_rods))
        print(
            f"Число удочек: {number_of_rods}, "
            f"Общее время: {time.perf_counter() - start_time:.2f} сек."
        )
