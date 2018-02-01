FROM python:3.5.2-alpine

 RUN    apk add --update --no-cache \
        postgresql-dev \
        build-base \
        bash \
        bash-doc \
        bash-completion

 ENV PYTHONUNBUFFERED 1
 RUN mkdir -p /usr/src/app
 WORKDIR /usr/src/app
 ADD requirements/requirements.txt /usr/src/app
 RUN pip install -r requirements.txt