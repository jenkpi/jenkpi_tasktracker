FROM python:3.13-slim

WORKDIR /app

ENV PYTHONPATH=app/src

COPY ./src /app/src
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]