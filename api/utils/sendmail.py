from fastapi_mail import  FastMail, MessageSchema, ConnectionConfig
from fastapi import BackgroundTasks
import os
from dotenv import load_dotenv

load_dotenv()

class Envs():
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_TLS = os.getenv("MAIL_TLS")
    MAIL_FROM =os.getenv("MAIL_FROM")
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")
    MAIL_PORT = os.getenv("MAIL_PORT")

conf = ConnectionConfig(
    MAIL_USERNAME = Envs.MAIL_USERNAME,
    MAIL_PASSWORD = Envs.MAIL_PASSWORD,
    MAIL_FROM = Envs.MAIL_FROM,
    MAIL_PORT = Envs.MAIL_PORT,
    MAIL_SERVER = Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER= "api/templates"
)

# conf = ConnectionConfig(
#     MAIL_USERNAME = "test@codeassociates.co.ke",
#     MAIL_PASSWORD = "Mweruli1996",
#     MAIL_FROM = "test@codeassociates.co.ke",
#     MAIL_PORT = 587,
#     MAIL_SERVER = "mail.codeassociates.co.ke",
#     MAIL_TLS = True,
#     MAIL_SSL = False,
#     USE_CREDENTIALS = True,
#     VALIDATE_CERTS = True,
#     TEMPLATE_FOLDER="api/templates"
# )

def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fm = FastMail(conf)

    background_tasks.add_task(
        fm.send_message, message, template_name='email.html')


async def send_registration_email(subject: str, email_to: str, body: dict):
    message =  MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message=message, template_name="email.html")