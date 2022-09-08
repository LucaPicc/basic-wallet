FROM python:3.10.6-buster


COPY ./backend/poetry.lock ./backend/pyproject.toml ./

ENV PATH="${PATH}:/root/.poetry/bin"

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

COPY ./backend/backend ./app

WORKDIR /app