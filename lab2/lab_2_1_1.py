import random


def get_random_ipv4() -> str:
    return ".".join([str(num()) for _ in range(4)])


def num() -> int:
    return random.randint(0, 255)


def write_ipv4(file: str) -> None:
    with open(file, "w") as file:
        for _ in range(10000):
            file.write(f"{get_random_ipv4()}\n")


write_ipv4("info.log")