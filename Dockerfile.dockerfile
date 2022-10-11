# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

COPY . ./app
WORKDIR /app

CMD ["python3", "lab1-aeom.py"]