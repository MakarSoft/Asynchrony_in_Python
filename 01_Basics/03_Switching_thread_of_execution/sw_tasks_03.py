# sw_tasks_03.py
# Использование deque

from time import sleep
from collections import deque


def task_1():
    for i in range(1, 5):
        print("число ->", i)
        yield


def task_2():
    for s in "№;%:?*":
        print("символ ->", s)
        yield


def task_3():
    for v in "абв":
        print("буква ->", v)
        yield


g1 = task_1()
g2 = task_2()
g3 = task_3()

# инициализируем очередь используя кортеж генераторов
tasks = deque((g1, g2, g3))
while tasks:
    sleep(0.2)
    task = tasks.popleft()  # извлекаем задачу с левого конца очереди
    try:
        next(task)
    except StopIteration:
        pass
    else:
        tasks.append(task)  # добавляем задачу в правый конец очереди
