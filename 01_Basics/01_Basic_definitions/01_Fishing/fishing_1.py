# Ловля рыбы одной удочкой
# Всего N_FISHERMEN рыбаков
# Каждый рыбок должен поймать по N_FISH рыб
# т.е. нам надо поймать N_FISHERMEN*N_FISH
# На поимку каждой рыбы уходит от 1 до 5 секунд

from time import sleep
from itertools import count
from random import randrange

N_FISHERMEN: int = 3    # количество рыбаков
N_FISH: int = 3         # сколько рыб должен поймать каждый рыбак

total_count = count(1)  # общее число выловленных рыб


class Fisherman:
    """ Рыбак """

    def __init__(self, name: str = "") -> None:
        self.name = name

    def get(self) -> None:
        # имитируем ожидание клева
        sleep(randrange(1, 5))

        # выводим результат улова
        print(f"{self.name} поймал одну. [Всего поймано: {next(total_count)}]")


def main(
    n_men: int = N_FISHERMEN,
    n_fish: int = N_FISH
) -> None:
    # создаем рыбаков
    fishermen = [Fisherman(f"Рыбак_№{i}") for i in range(1, n_men+1)]

    # ловим, пока каждый не поймает по {n_fish} рыб
    for _ in range(n_fish):
        # каждый по очереди ловит по 1 рыбе
        for f in fishermen:
            f.get()


if __name__ == "__main__":
    main()
