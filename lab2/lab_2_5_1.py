import os


def search_files(path_file: str, user_str: str) -> str:
    files_count = len(
        [0 for file in os.listdir(path_file) if user_str in file]
    )
    return f"Файлов находящихся в директории - {path_file}, имеющих подстроку - {user_str} -> {files_count}"


print(search_files("example", "0"))