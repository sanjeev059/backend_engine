FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
RUN apt-get install -y \
        libsasl2-dev \
        python-dev \
        libldap2-dev \
        libssl-dev

ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirnment.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000
RUN cd /usr/src/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
