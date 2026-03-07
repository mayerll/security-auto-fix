
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install pip-audit pytest

CMD ["python3", "cli.py"]
