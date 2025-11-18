import smtplib
import os
from email.message import EmailMessage

print("🔍 DEBUG: Starting email script...")
print(f"DEBUG: Environment IMAGE_PATH = {os.getenv('IMAGE_PATH')}")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SEND_TO = os.getenv("SEND_TO")
IMAGE_PATH = os.getenv("IMAGE_PATH")

print(f"DEBUG: SMTP Server = {SMTP_SERVER}")
print(f"DEBUG: Send To = {SEND_TO}")
print(f"DEBUG: Looking for image at: {IMAGE_PATH}")

if not IMAGE_PATH:
    raise ValueError("ERROR: IMAGE_PATH environment variable is missing.")

# Check file existence in container
print("DEBUG: Listing current directory contents:")
print(os.listdir("."))

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"ERROR: Image not found in container: {IMAGE_PATH}")

msg = EmailMessage()
msg["Subject"] = "New Image Uploaded to GitHub Repository"
msg["From"] = SMTP_USERNAME
msg["To"] = SEND_TO.split(",")
msg.set_content("A new image was uploaded. Attached below.")

print(f"DEBUG: Opening image file: {IMAGE_PATH}")

with open(IMAGE_PATH, "rb") as f:
    file_data = f.read()
    file_name = os.path.basename(IMAGE_PATH)
    ext = file_name.split(".")[-1].lower()

    print(f"DEBUG: Attaching image: {file_name}, type: {ext}")

    msg.add_attachment(
        file_data,
        maintype="image",
        subtype=ext,
        filename=file_name
    )

print("DEBUG: Connecting to SMTP server...")

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.starttls()
    print("DEBUG: Logged into email server...")
    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtp.send_message(msg)

print("🎉 SUCCESS: Email sent successfully!")

