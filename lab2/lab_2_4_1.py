import os
import random
import string


def create_dir(path: str) -> None:
    os.mkdir(path)


def create_file(name_dir: str) -> None:
    filename = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    with open(f"{name_dir}/{filename}.txt", "w") as file:
        file.write(filename)


def create_1000_files() -> None:
    name_dir = "example"
    create_dir(name_dir)
    for size in range(1, 1000):
        create_file(name_dir)


create_1000_files()
