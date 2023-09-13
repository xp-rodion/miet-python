import random


def get_random_ipv4() -> str:
    return f"{num()}.{num()}.{num()}.{num()}\n"


def num() -> int:
    return random.randint(0, 255)


def write_ipv4(file: str):
    with open(file, "w") as file:
        for _ in range(10000):
            file.write(get_random_ipv4())


write_ipv4("info.log")