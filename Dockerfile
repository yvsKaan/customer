FROM python:3.8


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirement.txt ./requirement.txt
RUN pip install -r ./requirement.txt

COPY . .
