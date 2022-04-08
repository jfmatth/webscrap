FROM python:3.8 AS PIPENV

WORKDIR /usr/src/pipenv
COPY Pipfile Pipfile.lock /usr/src/pipenv/

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt

FROM python:3.8-slim-buster
WORKDIR /usr/src/app

COPY --from=PIPENV /usr/src/pipenv/requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

ENTRYPOINT ["waitress-serve"]
CMD ["--host=0.0.0.0", "--port=80", "webscraps.wsgi:application"]