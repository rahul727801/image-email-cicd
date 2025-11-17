FROM python:3.10-slim

WORKDIR /app

COPY send_email.py .
COPY myimage.png .

RUN pip install smtplib email

CMD ["python", "send_email.py"]

