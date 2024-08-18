FROM python:3.10-slim

WORKDIR /workdir

COPY ./app /workdir/app
COPY ./pyproject.toml /workdir/
COPY ./poetry.lock /workdir/

RUN pip install poetry && poetry install --no-dev

CMD ["poetry", "run", "python", "/workdir/app/kafka_producer.py"]
