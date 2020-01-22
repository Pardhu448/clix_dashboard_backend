FROM python:3.6-alpine

#RUN useradd -r -u 900 -m -c "clix_dashboard_backend account" -d /home/clix_dashboard_backend -s /bin/false clix_dashboard_backend
RUN adduser -D clix_dashboard_backend

WORKDIR /home/clix_dashboard_backend

COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    py-cffi \
    && venv/bin/pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps
RUN apk --no-cache add libpq
#RUN venv/bin/pip install --no-cache-dir -r requirements.txt
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN venv/bin/pip install --no-cache-dir gunicorn psycopg2

COPY app app
COPY migrations migrations
COPY SchoolImages SchoolImages
COPY clix_dashboard_backend.py config.py entrypoint.sh ./

ARG DOCKER_UID 

RUN apk --no-cache add shadow && \ 
    usermod -u ${DOCKER_UID} clix_dashboard_backend \
    && groupmod -g ${DOCKER_UID} clix_dashboard_backend \
    && echo "Set clix_dashboard_backend's uid to ${DOCKER_UID}"


RUN chmod a+x entrypoint.sh

ENV FLASK_APP clix_dashboard_backend.py

RUN chown -R clix_dashboard_backend:clix_dashboard_backend ./
USER clix_dashboard_backend

EXPOSE 5000
#CMD ["flask", "run"]
#RUN source venv/bin/activate \
#    && flask db init --directory migration \
#    && mkdir migrations \
#    && mv migration/* migrations/ \
#    && deactivate

ENTRYPOINT ["./entrypoint.sh"]
