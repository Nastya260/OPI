import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiosmtplib import SMTP
from telebot import TeleBot


class Bot_telegram:
    """
    describes telegram bot
        bot_name - telegram bot
        email - cinema's email
        pwd - temporary password for email

    def send_ticket: void
        parameters:
        user_email:string - email of user who has bought ticket
        ticket_id:int - number of bought ticket
    """

    def __init__(self):
        self.bot_name = TeleBot(token='6596089373:AAF0WXjtUJoj8mWihdlF8c6KK5u7kmUmxj4')
        self.email = 'ourcinema@ukr.net'
        self.pwd = 'AfYPoASgrMTKmaoE'

    async def send_ticket(self, user_email, ticket_id):
        # send email with SMTP
        email_message = MIMEMultipart("your ticket`s id = " + str(ticket_id) + "<br>")
        email_message["From"] = self.email
        email_message["To"] = user_email
        email_message["Subject"] = f"Your ticket's ID: {ticket_id}"
        email_message.attach(MIMEText(f"<html><body>{email_message}</body></html>", "html", "utf-8"))

        smtp_client = SMTP(hostname="smtp.ukr.net", port=465, use_tls=True)
        async with smtp_client:
            await smtp_client.login(self.email, self.pwd)
            await smtp_client.send_message(email_message)

        # send mail with telegram


if __name__ == '__main__':
    c = Bot_telegram()
    asyncio.run((c.send_ticket('example@gmail.com', 13)))
    c.bot_name.polling()
