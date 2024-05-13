FROM python:3.12.3-slim

WORKDIR /app

COPY src/ /app/

RUN pip install kybra

CMD ["python", "main.py"]
