FROM python:3.11

RUN apt-get update && \
    apt-get install -y supervisor && \
    apt-get clean


WORKDIR /app

COPY . /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


RUN pip install --upgrade pip

RUN pip install -r requirements/requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["/usr/bin/supervisord"]
