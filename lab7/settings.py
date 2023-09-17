import environ

env = environ.Env()

environ.Env.read_env(".env")

EMAIL_LOGIN = env("EMAIL_LOGIN")
EMAIL_PASSWORD = env("EMAIL_PASSWORD")
SMTP_HOST = env("SMTP_HOST")
SMTP_PORT = env("SMTP_PORT")
IMAP_HOST = env("IMAP_HOST")
IMAP_PORT = env("IMAP_PORT")