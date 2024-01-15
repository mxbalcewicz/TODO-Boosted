# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/boosted

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install netcat
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/boosted/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/boosted/entrypoint.sh

# copy project
COPY . /usr/src/boosted/

# chmod entrypoint.sh issue on linux
RUN chmod +x /usr/src/boosted/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/boosted/entrypoint.sh"]