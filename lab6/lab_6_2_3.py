import time

from threading import Thread, Event


def example_task(event: Event):
    print("Запуск задачи, ожидание, когда событие будет в сигнальном состоянии")
    event.wait()
    print("Задача запущена! Событие перешло в сигнальное состояние")


event = Event()
thread = Thread(target=example_task, args=(event, ))

thread.start()

# Имитация работы какого-нибудь условия/действия
time.sleep(5)

event.set()

thread.join()