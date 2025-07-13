# Agentic AI K8s

This project provides a containerized Python application ready for deployment, using FastAPI and Uvicorn. The following instructions will help you build and run the application using Docker.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.

## Build the Docker Image

Open a terminal in the project directory and run:

```sh
docker build -t agentic-ai-k8s .
```

This command builds the Docker image and tags it as `agentic-ai-k8s`.

## Run the Docker Container

To start the application, run:

```sh
docker run -p 8080:8080 agentic-ai-k8s
```

This maps port 8080 on your host to port 8080 in the container.

## Application Details

- The application uses a non-root user (`myuser`) for security.
- The entrypoint runs Uvicorn to serve the FastAPI app defined in `main.py` on port 8080.
- All dependencies are installed from `requirements.txt`.

## File Structure

```
.
├── dockerfile
├── requirements.txt
├── main.py
└── (other source files)
```

## Customization

- To change the application port, update the `CMD` line in the `dockerfile`.
- Add or update dependencies in `requirements.txt` as needed.

---

**Note:** For production deployments, consider using orchestration tools like Kubernetes and follow best practices for environment variables and secrets
