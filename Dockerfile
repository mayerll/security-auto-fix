
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir pip-audit

COPY scanner/ scanner/
COPY reporter/ reporter/
COPY cli.py .

CMD ["python3", "cli.py", "scan", "."]
