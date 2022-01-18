FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Agrochain

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .