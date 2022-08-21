import os
from smtplib import SMTP
from twilio.rest import Client
MY_EMAIL = "your email"
MY_PASSWORD = "here comes pw "
ACCOUNT_SID = "AC57e51029499da84acf401b735f9f6c62"
AUTH_TOKEN = "543fdf8c5ac68a4a90ae8156b9f4e62d"
MY_NUM = "+num"
NUM = "+num"
class NotificationManager:

    def send(self, msg):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(body=msg, from_=MY_NUM,to=NUM)
        print(message.sid)

    def mail(self, msg, name):
        with SMTP("smpt.outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=name, msg=msg)


