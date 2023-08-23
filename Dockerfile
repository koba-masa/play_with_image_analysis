FROM python:3.11.4

USER root
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install
