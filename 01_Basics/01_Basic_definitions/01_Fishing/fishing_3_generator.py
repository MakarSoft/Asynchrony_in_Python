
# Один из вариантов рыбалки с использованием генераторов
# Один рыбак и 9 удочек.

from collections import deque
from random import randrange
from time import perf_counter
from typing import Generator

NUMBERS_OF_ROADS = 9


class Fisherman:
    """ Рыбак """

    def __init__(
        self,
        name: str = "Рыбак",
        number_of_fishing_rods: int = NUMBERS_OF_ROADS
    ) -> None:

        self.name = name  # имя рыбака
        self.number_of_fishing_rods = number_of_fishing_rods  # кол-во удочек

        self._fishing_rods: deque[Generator[bool, None, None]] = deque()
        self.total_caught = 0

        self.__init_catching()

    def __init_catching(self) -> None:
        # создаем список задач из генераторов-удочек

        for rod_number in range(1, self.number_of_fishing_rods + 1):

            self._fishing_rods.append(
                FishingRod(
                    rod_number=rod_number,
                    waiting_time=randrange(1, 11),
                    fisher=self
                ).catch()
            )

    def fishing_loop(self) -> None:

        # цикл событий
        while self._fishing_rods:
            # забрасываем первую удочку из очереди
            fishing_rod = self._fishing_rods.popleft()

            # поймали рыбу? (проверка завершения выполнения задачи)
            if not next(fishing_rod):
                # возвращаем удочку в очередь
                self._fishing_rods.append(fishing_rod)


class FishingRod:
    """ Удочка """

    def __init__(self, rod_number: int, waiting_time: int, fisher: Fisherman):
        self.rod_number = rod_number    # номер удочки
        self.waiting_time = waiting_time    # время ожидания клёва
        self.fisher = fisher    # рыбак

    def catch(self) -> Generator[bool, None, None]:
        """ Забрасываем удочку """

        start = perf_counter()
        while True:
            if perf_counter() - start >= self.waiting_time:
                self.fisher.total_caught += 1
                print(
                    f"{self.fisher.name} поймал одну, "
                    f"[Всего поймано: {self.fisher.total_caught}]"
                )
                print(
                    f"\tпоймано на удочку №{self.rod_number} "
                    f"после ожидания в течение {self.waiting_time} сек."
                )
                # передаем контроль управления в цикл событий
                # с пометкой завершения задачи
                yield True
            # передаем контроль управления в цикл событий
            # с пометкой ожидания завершения задачи
            yield False


def main(
    name: str = "Борщёв",
    number_of_fishing_rods: int = NUMBERS_OF_ROADS
) -> None:

    start_time = perf_counter()
    fisher = Fisherman(name, number_of_fishing_rods)
    fisher.fishing_loop()

    print(f"\nОбщее время: {perf_counter() - start_time:.2f} сек.")


if __name__ == "__main__":
    main()
