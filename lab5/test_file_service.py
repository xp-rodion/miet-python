import pytest
from lab5.file_service import FileService
from lab5.len_exception import LengthError


class TestFileService:

    @pytest.fixture(scope="class")
    def data(self):
        return b'privet, kak dela'

    @pytest.fixture(scope="class")
    def file(self, data):
        f_name = "text.txt"
        with open(f_name, "wb") as f:
            f.write(data)
        return f_name

    @pytest.fixture(scope="class")
    def file_service(self, file):
        return FileService(file=file)

    def test_open_file(self, file_service, data):
        file_service.read_file()
        assert file_service.storage == data

    def test_file_not_found(self, file_service):
        file_service.file = "aaa.txt"
        file_service.read_file()

    def test_file_length(self, file_service):
        file_service.file = "bbb.txt"
        file_service.read_file()

    def test_write(self, file_service, data):
        file_service.write_from_restored_data("text_output.txt")
        with open("text_output.txt", "rb") as f:
            assert data == f.read()