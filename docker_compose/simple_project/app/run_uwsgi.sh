#!/usr/bin/env bash

set -e

cd .
python ./manage.py collectstatic --no-input

chown www-data:www-data /var/log

uwsgi --strict --ini /etc/app/uwsgi.ini
