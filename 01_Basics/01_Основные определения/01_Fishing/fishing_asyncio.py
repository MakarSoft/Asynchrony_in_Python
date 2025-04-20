# Используем asyncio

import asyncio
import random
from time import perf_counter


class Fisherman:
    """ Рыбак """

    name: str = "Рыбак"
    total_caught: int = 0

    async def fish(
        self,
        rod_number: int,
        wait_time: int
    ) -> None:
        """Асинхронная задача для ловли рыбы."""

        await asyncio.sleep(wait_time)
        self.total_caught += 1
        print(
            f"{self.name} поймал одну, "
            f"всего: {self.total_caught}"
        )
        print(
            f"\tНа удочке №{rod_number} "
            f"после {wait_time} сек. ожидания"
        )


async def main():

    fisherman = Fisherman()
    # Создаем 9 удочек с разными временами ожидания
    tasks = [
        fisherman.fish(rod_num, random.randint(1, 10))
        for rod_num in range(1, 10)
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = asyncio.get_event_loop().time()
    asyncio.run(main())
    print(f"Общее время: {perf_counter() - start_time:.2f} сек.")
