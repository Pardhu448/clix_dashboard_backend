# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --no-cache gcc python3-dev musl-dev postgresql-dev libffi-dev py-cffi libpq \
    && mkdir /home/clix_dashboard_backend

# set work directory
WORKDIR /home/clix_dashboard_backend

# copy project code and required file as well as directories
COPY ./app/ /home/clix_dashboard_backend/app/

# copy project code and required file as well as directories
COPY ./requirements.txt ./clix_dashboard_backend.py ./config.py ./entrypoint.sh /home/clix_dashboard_backend/

# install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["sh", "/home/clix_dashboard_backend/entrypoint.sh"]
