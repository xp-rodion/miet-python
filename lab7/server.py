import socket
import pickle

from common import NetworkConnection
from sender import Sender
from email.message import EmailMessage


class Server(NetworkConnection):
    COUNT = 0

    def __new__(cls, *args, **kwargs):
        cls.COUNT += 1
        return super().__new__(cls)

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
            srv.bind((self.HOST, self.PORT))
            srv.listen(1)
            conn, addr = srv.accept()
            bytes_false, bytes_true = pickle.dumps(False), pickle.dumps(True)
            print("Начинаю прослушку порта")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        continue
                    decode_data = pickle.loads(data)
                    email = decode_data["email"]
                    msg = decode_data["msg"]

                    print(f"Принял данные! email - {email}: msg - {msg}")

                    if not data:
                        conn.sendall(bytes_false)

                    if {type(email), type(msg)} != {str}:
                        conn.sendall(bytes_false)

                    if "@" not in email:
                        conn.sendall(bytes_false)

                    try:
                        print("Отправляю сообщение")
                        self.send_msg(msg, email)
                        conn.sendall(bytes_true)

                    except Exception as e:
                        print(f"Ошибка - {e}")
                        conn.sendall(bytes_false)

    def create_msg(self, user_email: str, message: str):
        msg = EmailMessage()
        msg["Subject"] = f"[Ticket #{self.COUNT}] Mailer"
        msg["To"] = user_email
        msg.set_content(message)
        return msg

    def send_msg(self, msg: str, user_email: str):
        message = self.create_msg(user_email=user_email, message=msg)
        sender = Sender(user_email, message)
        sender.send_msg()


def start_server():
    srv = Server()
    srv.listen()


# start_server()
srv = Server()
srv.listen()