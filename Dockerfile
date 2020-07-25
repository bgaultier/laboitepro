FROM python:3.8-alpine
MAINTAINER LaBoîte Team <support@laboite.cc>
EXPOSE 8000
RUN apk add gcc jpeg-dev libc-dev libpng-dev libxml2-dev libxslt-dev zlib-dev
ADD . /lenuage
RUN cd /lenuage \
    && pip install -r requirements/requirements.txt
WORKDIR /lenuage
CMD cd /lenuage \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata sites \
    && DJANGO_SUPERUSER_PASSWORD="admin" python manage.py createsuperuser --username admin --email root@localhost --noinput \
    && python manage.py runserver 0.0.0.0:8000
