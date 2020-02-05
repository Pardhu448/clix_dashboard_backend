#!/bin/sh
# this script is used to boot a Docker container


echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

if [[ -d /home/clix_dashboard_backend/migrations ]]; then
  echo "Migration folder already exists."
else
  echo "Migration folder doesn't exists. "
  echo "Hence triggering flask db init."
  flask db init;
  echo "And triggering flask db migrate."
  flask db migrate;
fi

flask create_admin --username admin_clixdata --password clixdata --email admin@clix_dashboard_backend.com ;

while true; do
    flask db upgrade;
    if [[ "$?" == "0" ]]; then
      break
    fi
    echo "Deploy command failed, retrying in 5 secs..."
    sleep 5
done

if [[ $FLASK_ENV == "prduction" ]]
  c_file="/home/clix_dashboard_backend/certs/cert.pem"
  k_file="/home/clix_dashboard_backend/certs/key.pem"
  if [[ -f ${c_file} ]] && [[ -f ${k_file} ]]; then
    ssl_parameters = "--certfile=${c_file} --keyfile=${k_file}"
  else
    echo "Files missing - ${c_file} and ${k_file}"
  fi
fi

# starting gunicorn service on port 5000
echo "Starting gunicorn service on port 5000"
exec gunicorn ${ssl_parameters} -b 0.0.0.0:5000 --access-logfile - --error-logfile - clix_dashboard_backend:app

# exec "$@"