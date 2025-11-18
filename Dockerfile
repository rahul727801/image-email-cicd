FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Debug: show files inside container
RUN echo "🔍 DEBUG: Files inside /app:" && ls -R /app

CMD ["python", "send_email.py"]

