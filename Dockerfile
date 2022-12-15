FROM python:slim-buster

LABEL maintainer="Sasha Alimov klimdos@gmail.com"

WORKDIR /app

COPY src .

ADD data.json data.json

RUN pip install -r requirements.txt

ARG BUILD

ENV BUILD=$BUILD

EXPOSE 8080

CMD ["uvicorn", "app:main", "--host", "0.0.0.0", "--port", "8080"]
