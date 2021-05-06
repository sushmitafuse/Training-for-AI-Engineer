FROM python:3.8.10-slim-buster

EXPOSE 5000
RUN mkdir /app

WORKDIR /app

COPY pyproject.toml /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

CMD ["python3", "app.py"]