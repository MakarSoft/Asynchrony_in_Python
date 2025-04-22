# sw_tasks_01.py
# Использование списка задач (бесконечные задачи)

import time


def task_1():
    while True:
        print("задача 1")
        yield


def task_2():
    while True:
        print("задача 2")
        yield


def task_3():
    while True:
        print("задача 3")
        yield


g1 = task_1()
g2 = task_2()
g3 = task_3()
tasks = [g1, g2, g3]

# выполняем задачи до тех пор, пока они есть в списке
while tasks:
    time.sleep(0.2)
    task = tasks.pop(0)  # извлекаем задачу из списка
    next(task)  # выполняем задачу
    tasks.append(task)  # добавляем задачу обратно в список задач
