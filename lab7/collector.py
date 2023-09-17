import quopri

from imaplib import IMAP4_SSL
from common import Auth
from settings import IMAP_HOST, IMAP_PORT


class Collector(Auth):
    IMAP_HOST = IMAP_HOST
    IMAP_PORT = IMAP_PORT

    def __init__(self):
        self.success = "success_request.log"
        self.error = "error_request.log"

    def check_correct_letter(self):
        with IMAP4_SSL(host=IMAP_HOST, port=IMAP_PORT) as M:
            rc, resp = M.login(self.EMAIL, self.PASSWORD)
            M.select()
            typ, data = M.search(None, 'ALL')
            for num in data[0].split():
                typ, data = M.fetch(num, '(RFC822)')
                mail = quopri.decodestring(data[0][1]).decode("utf-8", errors="ignore")
                self.search_ticket_mail(mail)

    @staticmethod
    def search_ticket_mail(data: str):
        lst_data = list(filter(lambda x: len(x) > 1, data.split("\n")))
        for entry in lst_data:
            if "Ticket" in entry:
                ID = "".join([symb for symb in entry if symb.isdigit()])
                with open("success_request.log", "a") as file:
                    file.write(f"ID: {ID} - Message: {lst_data[-1]}\n")
                    return

        with open("error_request.log", "a") as file:
            file.write(f"Error - {lst_data[-1]}\n")


collector = Collector()
collector.check_correct_letter()