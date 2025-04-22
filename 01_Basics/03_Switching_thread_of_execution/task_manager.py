from collections import deque
from collections.abc import Iterable, Generator

Gen = Generator[int | str, None, None]


def task_1() -> Generator[int, None, None]:
    for i in range(1, 5):
        yield i


def task_2() -> Generator[str, None, None]:
    for s in "AB":
        yield s


class IntGenerator:
    def __init__(self, n: int = 5) -> None:
        self.n = n  # Максимальное значение

    def __iter__(self) -> Generator[int, None, None]:
        current = 0
        while current < self.n:  # Генерируем числа от 1 до n
            current += 1
            yield current  # Возвращаем текущее значение


def task_manager(tasks: Iterable[Gen]) -> None:

    tasks = deque(tasks)

    while tasks:
        task = tasks.popleft()

        try:
            res = next(task)
            print(res)
        except StopIteration:

            # MyPy - ругается (но код работает):
            # "Generator[int | str, None, None]" has no attribute "__name__"
            # print(f"Задача {task.__name__} завершена!")

            # print(f"Задача {task.gi_code.co_name} завершена!")

            task_name = (
                task.__name__
                if hasattr(task, '__name__')
                else "Unnamed Task"
            )
            print(f"Задача {task_name} завершена!")

            continue

        tasks.append(task)


# ----------------------------------------------------------


if __name__ == "__main__":
    g1 = task_1()
    g2 = task_2()
    g3 = (x for x in range(1, 3))
    g4 = iter(IntGenerator(5))
    g5 = (lambda: (yield 42))()

    task_manager((g1, g2, g3, g4, g5))
