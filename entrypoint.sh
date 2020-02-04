#!/bin/sh
# this script is used to boot a Docker container
source venv/bin/activate
#flask db migrate
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
      break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
exec gunicorn --certfile=/home/clix_dashboard_backend/app/certificates/cert.pem --keyfile=/home/clix_dashboard_backend/app/certificates/key.pem -b 0.0.0.0:5000 --access-logfile - --error-logfile - clix_dashboard_backend:app
