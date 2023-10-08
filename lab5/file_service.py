from lab5.len_exception import LengthError


class FileService:

    def __init__(self, file: str):
        self.file = file
        self.storage = None

    def read_file(self):
        try:
            file = open(self.file, "rb")
            data = file.read()
            self.validate_length(data)
            self.storage = data
            file.close()
        except LengthError as e:
            print(f"Ошибка {e} - длина в данных файла некорректна")
        except FileNotFoundError as e:
            print(f"Ошибка {e} - файл не найден")
        except IOError as e:
            print(f"Ошибка {e} - в чтении файла")

    @staticmethod
    def validate_length(data):
        if len(data) > 0:
            return data
        raise LengthError("Длина должна быть положительной")

    def write_from_restored_data(self, file: str):
        try:
            output_file = open(file, "wb")
            output_file.write(self.restored_data)
            output_file.close()
        except IOError as e:
            print(f"Ошибка {e} - в записи файла ошибка")
        except TypeError as e:
            print(f"Ошибка {e} - тип данных некорректный")

    @property
    def restored_data(self):
        return self.storage