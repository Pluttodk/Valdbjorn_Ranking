FROM python:3.12.3-slim-bullseye

RUN pip install --upgrade pip

WORKDIR /app

RUN pip install pdm

ADD pyproject.toml *.lock *.env README* /app

ADD src /app/src

RUN pdm install --prod

CMD ["pdm", "run", "src/ranking.py"]