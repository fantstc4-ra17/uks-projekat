FROM python:3.5.2-alpine
 ARG DEPLOY=0
 RUN    apk add --update --no-cache \
        postgresql-dev \
        build-base \
        bash \
        bash-doc \
        bash-completion

 ENV PYTHONUNBUFFERED 1
 RUN mkdir -p /usr/src/app
 WORKDIR /usr/src/app
 COPY app/. /usr/src/app

 RUN if [ $DEPLOY -eq 0 ]; then rm -r /usr/src/app/*; fi

 COPY requirements/requirements.txt .
 RUN pip install -r requirements.txt