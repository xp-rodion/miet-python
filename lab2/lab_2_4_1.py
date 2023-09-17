import os


def create_dir(path: str) -> None:
    os.mkdir(path)


def create_file(name_dir: str, volume: int) -> None:
    with open(f"{name_dir}/{volume}.txt", "wb") as file:
        file.write(os.urandom(volume*1024))


def create_100_files() -> None:
    name_dir = "test"
    create_dir(name_dir)
    for size in range(1, 101):
        create_file(name_dir, size)


create_100_files()
