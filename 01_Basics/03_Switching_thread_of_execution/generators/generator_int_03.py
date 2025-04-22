from collections.abc import Generator

# Если нужно многоразовое итерирование:
# Используйте отдельный генератор в __iter__:


class IntGenerator:
    def __init__(self, n: int = 5) -> None:
        self.n = n

    def __iter__(self) -> Generator[int, None, None]:
        current = 0
        # Генерируем числа от 1 до n
        while current < self.n:
            current += 1
            yield current

# каждый вызов iter() создает новый генератор .
# Объект можно перебирать многократно


g = IntGenerator(2)
print(list(g))  # [1, 2]
print(list(g))  # [1, 2] (создается новый генератор)
