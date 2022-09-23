import smtplib

from email.mime.text import MIMEText

import config


def send_email(message: str):
    sender = config.sender
    password = config.authentification_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender, config.receiver, msg.as_string())

        return 'OK'
    except Exception as ex:
        return ex

