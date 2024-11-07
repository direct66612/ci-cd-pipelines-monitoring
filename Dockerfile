FROM python:3.8-slim

COPY app.py /app/app.py

WORKDIR /app

CMD ["python", "app.py"]

