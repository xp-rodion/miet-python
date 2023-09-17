import os


def search_files(path_file: str, left: int, right: int) -> str:
    files_count = len(
        [0 for file in os.listdir(path_file) if (os.stat(f"{path_file}/{file}").st_size / 1024) in range(left, right + 1)]
    )
    return f"Файлов находящихся в директории - {path_file}, в диапазоне [{left}; {right}] - {files_count} штук"


print(search_files(input("Название директории: "), int(input("Левая граница: ")), int(input("Правая граница: "))))