FROM python:3.10

WORKDIR /opt/app

ENV DJANGO_SETTINGS_MODULE=example.settings

COPY app/run_uwsgi.sh run_uwsgi.sh
COPY app/requirements.txt requirements.txt
COPY uwsgi.ini /etc/app/uwsgi.ini

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY app/ .

EXPOSE 8000

RUN chmod +x ./run_uwsgi.sh

CMD ["./run_uwsgi.sh"]