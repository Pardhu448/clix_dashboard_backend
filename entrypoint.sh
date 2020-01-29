#!/bin/sh
# this script is used to boot a Docker container


echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

flask db init;
flask db migrate;
flask create_admin --username admin_clixdata --password clixdata --email admin@clix_dashboard_backend.com ;

while true; do
    flask db upgrade;
    if [[ "$?" == "0" ]]; then
      break
    fi
    echo "Deploy command failed, retrying in 5 secs..."
    sleep 5
done

# starting gunicorn service on port 5000
echo "Starting gunicorn service on port 5000"
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - clix_dashboard_backend:app

# exec "$@"