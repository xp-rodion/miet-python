import os
import time

from threading import Thread


def create_size_file(path, count: int):
    with open(f"{path}/size.txt", "w") as file:
        file.write(str(count))
    os.remove(f"{path}/size.txt")


def search(path: str):
    lst_dir = os.listdir(path)
    if "size.txt" not in lst_dir:
        file_count = len([0 for file in lst_dir if "." in file])
        create_size_file(path, file_count)

    lst_with_dir = [file for file in lst_dir if "." not in file]
    for entry in lst_with_dir:
        search(f"{path}/{entry}")


st_time = time.time()
search("test")
end_time = time.time()
print("Время синхронного выполнения: ", end_time - st_time)


th1 = Thread(target=search, args=("test", ))
th2 = Thread(target=search, args=("test", ))

st_time = time.time()
th1.start(), th2.start()
end_time = time.time()
print("Время поток-го выполнения: ", end_time - st_time)