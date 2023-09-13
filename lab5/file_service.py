from len_exception import LengthError


class FileService:

    def __init__(self, file: str):
        self.file = file
        self.storage = None

    def read_file(self):
        try:
            file = open(self.file, "r")
            data = file.read()
            self.validate_data(data)
            self.validate_length(data)
            self.storage = data
            file.close()
        except LengthError as e:
            print(f"Ошибка {e} - длина в данных файла некорректна")
        except TypeError as e:
            print(f"Ошибка {e} - в данных файла")
        except Exception as e:
            print(f"Ошибка {e} - в чтении файла")

    @staticmethod
    def validate_data(data):
        if isinstance(data, str):
            return data
        raise TypeError("Тип данных некорректен")

    @staticmethod
    def validate_length(data):
        if len(data) > 0:
            return data
        raise LengthError("Длина должна быть положительной")

    def write_from_restored_data(self, file: str):
        try:
            output_file = open(file, "w")
            output_file.write(self.storage)
            output_file.close()
        except Exception as e:
            print(f"Ошибка {e} - в записи файла ошибка")

    @property
    def restored_data(self):
        return self.storage