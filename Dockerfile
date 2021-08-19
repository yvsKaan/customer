FROM python:3.8


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DATABASE_URL psql://postgres:test123@db:5432/dbcustomer

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirement.txt ./requirement.txt
RUN pip install -r ./requirement.txt

COPY . .
