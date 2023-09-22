import time
from multiprocessing import Pool
from math import sqrt


def timer(func):
    def wrapper(*args, **kwargs):
        st_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        dif_time = end_time - st_time
        print(f"{func.__name__} - {dif_time}")
        return result
    return wrapper


def formula(i: int, j: int):
    return sqrt((i - j) ** 2)


@timer
def sync_create_matrix(size: int) -> list[list]:
    return [[formula(i, j) for j in range(1, size + 1)] for i in range(1, size + 1)]


def create_row(data: tuple) -> list:
    i, size = data
    return [formula(i, j) for j in range(1, size + 1)]


@timer
def multiprocessing_create_matrix(size: int) -> list[list]:
    pool = Pool(4)
    return pool.map(create_row, [(i, size) for i in range(1, size + 1)])


sync_create_matrix(5000)
multiprocessing_create_matrix(5000)