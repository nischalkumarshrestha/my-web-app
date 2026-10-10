# Containerized Microservice

## Project Overview
A simple Python web application running inside a Docker container.

## Technologies Used
- Python
- Docker
- GitHub
- Docker Hub

## Features
- Displays the container hostname
- Displays the server timestamp
- Runs on port 8080
- Prepared for cloud deployment

## Run Locally
Build the Docker image:

```bash
docker build -t my-web-app:v1 .
```

Run the container:

```bash
docker run -d -p 8080:8080 --name my-cloud-service my-web-app:v1
```

Open http://localhost:8080 in your browser.

## Docker Hub
Image: nischalkshrestha/my-web-app:v1

## Source Code
https://github.com/nischalkumarshrestha/my-web-app
