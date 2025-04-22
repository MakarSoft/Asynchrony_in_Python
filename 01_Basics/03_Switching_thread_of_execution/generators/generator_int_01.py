from typing import Self

# Чтобы объект класса можно было использовать как генератор
# (как в генераторном выражении), нужно, чтобы он был итератором.
# Для этого надо реализовать методы __iter__ и __next__:


class IntGenerator:
    def __init__(self, n: int = 5) -> None:
        self.n = n
        self.current = 0  # Состояние итератора

    def __iter__(self) -> Self:
        return self  # Возвращаем себя как итератор

    def __next__(self) -> int:
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration  # Генерируем исключение при завершении

# __iter__ возвращает self — это делает объект итератором .
# __next__ управляет логикой генерации значений и выбрасывает
#          StopIteration при завершении.


g = IntGenerator(3)
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
try:
    print(next(g))  # StopIteration
except StopIteration:
    print("Генератор исчерпан")

# !!!
# Состояние хранится в объекте (self.current), а не внутри генератора.
# Итератор одноразовый — после завершения повторное использование
# объекта невозможно

g = IntGenerator(2)  # повторно инициируем итератор
for x in g:
    print(x)  # 1, 2
for x in g:
    print(x)  # Ничего не выведет (итератор уже исчерпан self.current == 2)
