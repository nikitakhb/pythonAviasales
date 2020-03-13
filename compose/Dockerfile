FROM python:3.8-alpine3.10

ENV PROJECT_ROOT=/application

COPY ./Pipfile.lock ./Pipfile $PROJECT_ROOT/

COPY ./app $PROJECT_ROOT/app

WORKDIR $PROJECT_ROOT

CMD ["python", "app"]