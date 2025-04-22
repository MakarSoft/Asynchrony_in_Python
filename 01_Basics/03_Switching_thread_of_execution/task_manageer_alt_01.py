from collections.abc import Iterable, Generator

Gen = Generator[int | str, None, None]


def task_1() -> Generator[int, None, None]:
    for i in range(1, 5):
        yield i


def task_2() -> Generator[str, None, None]:
    for s in "AB":
        yield s


def task_manager(tasks: Iterable[Gen]) -> None:

    SENTINEL: object = object()  # Константа для маркировки завершения
    active_tasks: list[Gen] = list(tasks)  # Список активных задач

    while active_tasks:

        # Итерируемся по копии, чтобы безопасно удалять задачи
        for task in active_tasks.copy():
            result = next(task, SENTINEL)

            if result is SENTINEL:
                # Определяем имя задачи, если доступно
                task_name = (
                    task.__name__
                    if hasattr(task, '__name__')
                    else "Unnamed Task"
                )
                print(f"Задача {task_name} завершена!")
                # Удаляем завершенную задачу из списка активных задач
                active_tasks.remove(task)
            else:
                print(result)


# ----------------------------------------------------------
if __name__ == "__main__":
    g1 = task_1()
    g2 = task_2()

    task_manager((g1, g2))
