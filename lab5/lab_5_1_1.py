from file_service import FileService


input_file = input("Введите название пользовательского файла: ")
output_file = input("Введите файл, в который нужно восстановить данные файла: ")
service = FileService(file=input_file)

service.read_file()
print("Данные с исходного файла", service.storage)

service.write_from_restored_data(output_file)
