# TODO Boosted

A playground project to utilize newest aspects of Django, apps that I haven't had the opportunity to write yet and to develop new skills.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your system:

1. Docker: Make sure you have Docker installed and running on your machine. You can download and install Docker from the official website: [https://www.docker.com/get-started](https://www.docker.com/get-started)

2. Git: If you don't have Git installed, you can download it from the official website: [https://git-scm.com/downloads](https://git-scm.com/downloads)

# Setup
## Build and Run the Project
Build the Docker Image:

From the root of the project directory, run the following command to build the Docker image:

    docker-compose build

## Update .env file from the repository
Example:

    DEBUG=0
    SECRET_KEY=83yvbpm$g3u6b7*&g1hh%^63q473a=rmp)xr=uxrtf^&&g^q=8
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=db
    SQL_USER=root
    SQL_PASSWORD=password
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres


## Create and Start Containers:

Run the following command to create and start the containers defined in the docker-compose.yml file:

    docker-compose up -d
The -d flag runs the containers in the background.

## Access the Application:

Once the containers are up and running, you can access the application in your web browser by visiting:

http://localhost:8000/
Your application should now be up and running!

## Stopping and Removing Containers
To stop and remove the containers, execute the following command:

    docker-compose down
This will gracefully stop and remove the containers, freeing up system resources.