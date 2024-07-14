from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USERNAME,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.SMTP_USERNAME,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)

async def send_activation_email(email: str, token: str):
    activation_link = f"http://localhost:8000/auth/activate?token={token}"
    message = MessageSchema(
        subject="Account Activation",
        recipients=[email],
        body=f"Please click the following link to activate your account: {activation_link}",
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)


    
