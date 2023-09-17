import pickle
import socket
from common import NetworkConnection


class Connect(NetworkConnection):

    def send_information(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
            """Connect to server"""
            print("Подключение к серверу")
            srv.connect((self.HOST, self.PORT))
            while True:
                mail, message = input("Введите пользовательскую почту: "), input("Введите сообщение пользователю: ")
                client = Client(mail, message)
                print("Отправка данных")
                srv.sendall(client.create_information())
                srv_response = srv.recv(1024)
                decode_response = pickle.loads(srv_response)
                print("Получил ответ!", decode_response)
                if decode_response:
                    break


class Client:

    def __init__(self, email: str, msg: str):
        self.email = email
        self.msg = msg

    def create_information(self):
        data = {
            "email": self.email,
            "msg": self.msg,
        }
        bytes_data = pickle.dumps(data)
        return bytes_data


cnt = Connect()
cnt.send_information()