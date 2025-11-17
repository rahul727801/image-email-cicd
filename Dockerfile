FROM python:3.10-slim

WORKDIR /app

COPY send_email.py ./

RUN pip install secure-smtplib

CMD ["python3", "send_email.py"]

