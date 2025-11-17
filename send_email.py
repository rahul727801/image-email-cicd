import smtplib
import os
from email.message import EmailMessage

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SEND_TO = os.getenv("SEND_TO")
IMAGE_PATH = os.getenv("IMAGE_PATH", "myimage.png")

msg = EmailMessage()
msg["Subject"] = "New Image from GitHub Docker CI/CD"
msg["From"] = SMTP_USERNAME
msg["To"] = SEND_TO.split(",")
msg.set_content("Attached is the latest image uploaded to the Git repository.")

with open(IMAGE_PATH, "rb") as f:
    file_data = f.read()
    file_name = os.path.basename(IMAGE_PATH)
    msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtp.send_message(msg)

print("Email sent successfully!")

