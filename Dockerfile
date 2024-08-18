FROM python:3.10-slim

WORKDIR /workdir 

COPY ./app /workdir/app
COPY ./pyproject.toml /workdir/

RUN pip install poetry && poetry install --no-dev

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
