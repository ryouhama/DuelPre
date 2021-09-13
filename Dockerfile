FROM python:3.8.1
RUN mkdir /app
RUN mkdir /app/library
WORKDIR /app
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip setuptools wheel
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

COPY pyproject.toml /app
RUN poetry install

COPY ./.env /app
