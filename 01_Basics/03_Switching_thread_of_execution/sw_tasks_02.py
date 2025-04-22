# sw_tasks_02.py
# Использование списка задач (конечные задачи)

from time import sleep


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

tasks = [g1, g2, g3]

while tasks:
    sleep(0.2)
    task = tasks.pop(0)
    try:
        next(task)  # пробуем получить новое значение от генератора
    except StopIteration:
        pass  # пропускаем цикл
    else:
        # возвращаем генератор в список, если он не возбудил StopIteration
        tasks.append(task)
