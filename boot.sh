#!/bin/bash
# start gunicorn when the container is started
source env/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - postit:app