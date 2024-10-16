# Docker Demo for Linux Club @ UCU

This repository contains a simple FastAPI application to demonstrate the basics of using Docker. It's designed as an educational resource for members of the Linux Club at Ukrainian Catholic University.

## Repository Structure

- `main.py`: Contains a basic FastAPI application with simple endpoints.
- `requirements.txt`: Lists the Python dependencies for the project.
- `Dockerfile`: Available only in the [`with-docker`](https://github.com/pmozil/docker-demo/tree/with-docker) branch.

## Finding the Dockerfile

To see the Dockerfile and explore the Docker setup:

1. Visit the [`with-docker`](https://github.com/pmozil/docker-demo/tree/with-docker) branch of this repository.
2. Look for the `Dockerfile` in the root directory of that branch.

This structure allows for a clear comparison between the basic application setup and its Dockerized version.

## Purpose

This demo aims to introduce the concept of containerization using Docker, showcasing how a simple Python web application can be packaged and run in a container. It serves as a practical example for understanding the basics of Docker in web development.


## Building and Running This App

To build and run this application using Docker, follow these steps:

1. Clone the repository and switch to the `with-docker` branch:
   ```
   git clone https://github.com/pmozil/docker-demo.git
   cd docker-demo
   git checkout with-docker
   ```

2. Build the Docker image:
   ```
   docker build -t fastapi-demo .
   ```

3. Run the Docker container:
   ```
   docker run -p 80:8000 fastapi-demo
   ```

4. Access the application:
   Open your web browser and navigate to `http://localhost` to see the FastAPI application running.

5. Explore the API documentation:
   Visit `http://localhost/docs` to access the automatically generated Swagger UI documentation for the FastAPI application.

Note: Make sure you have Docker installed on your system before following these steps. If you don't have Docker installed, you can download it from the [official Docker website](https://www.docker.com/get-started).
