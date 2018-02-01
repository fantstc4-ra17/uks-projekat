FROM python:3.5.2-alpine

 RUN    apk add --update --no-cache \
        postgresql-dev \
        build-base \
        bash \
        bash-doc \
        bash-completion

 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/