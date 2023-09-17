from smtplib import SMTP_SSL
from email.message import EmailMessage

from settings import SMTP_PORT, SMTP_HOST
from common import Auth


class Sender(Auth):
    SMTP_HOST = SMTP_HOST
    SMTP_PORT = SMTP_PORT

    def __init__(self, user_email: str, msg: EmailMessage):
        self.user_email = user_email
        self.msg = msg

    def send_msg(self):
        with SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.login(user=self.EMAIL, password=self.PASSWORD)
            self.msg["From"] = self.EMAIL
            smtp.send_message(self.msg)