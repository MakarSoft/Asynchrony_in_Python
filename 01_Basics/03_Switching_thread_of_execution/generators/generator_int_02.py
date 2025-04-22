from typing import Self


class IntGenerator:
    def __init__(self, n: int = 5) -> None:
        self.n = n
        self.current = 0  # Состояние итератора

    def __iter__(self) -> Self:
        self.current = 0
        return self  # Возвращаем себя как итератор

    def __next__(self) -> int:
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration  # Генерируем исключение при завершении


g = IntGenerator(2)  # инициируем итератор
for x in g:
    print(x, end=" ")  # 1, 2
print()

# состояние сбрасывается при __iter__
for x in g:
    print(x, end=" ")  # 1 2
print()
