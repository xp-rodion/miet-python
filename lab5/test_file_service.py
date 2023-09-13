import unittest
from file_service import FileService


class FileServiceTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.file_service = FileService("test.txt")
        with open("test.txt", "r") as file:
            self.data = file.read()

    def test_read_file(self):
        self.file_service.read_file()
        assert self.file_service.storage == self.data

    def test_write_restored_data(self):
        self.file_service.read_file()
        output_file = "test_output.txt"
        self.file_service.write_from_restored_data(output_file)
        with open(output_file, "r") as file:
            assert file.read() == self.file_service.storage


if __name__ == "__main__":
    unittest.main()