# Pull official base image
FROM python:3.11.4-slim-buster

# Set work directory
WORKDIR /usr/src/boosted

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/boosted/requirements.txt
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/boosted/entrypoint.sh

# Copy project
COPY . /usr/src/boosted/

# chmod entrypoint.sh issue on linux
RUN chmod +x /usr/src/boosted/entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/boosted/entrypoint.sh"]