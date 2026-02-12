# TaskPilot

TaskPilot is an open-source automation platform designed to be a simpler, self-hostable alternative to services like Zapier or Make. It allows you to connect different applications and automate workflows.

## Features

-   **Visual Workflow Editor:** (Coming Soon) A user-friendly interface for creating and managing automation flows.
-   **Extensible Connectors:** Easily add new services and triggers.
-   **Self-Hosted:** Full control over your data and infrastructure.
-   **Asynchronous Task-Processing:** Powered by Celery and Redis for reliable background job execution.

## Tech Stack

-   **Backend:** FastAPI, Celery, SQLAlchemy
-   **Frontend:** React, Tailwind CSS
-   **Database:** SQLite (for MVP), Redis
-   **Containerization:** Docker

## Getting Started

To get a local development environment up and running, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/J4HDx/TaskPilot.git
    cd TaskPilot
    ```

2.  **Create an environment file:**
    -   Copy the example environment file: `cp .env.example .env`
    -   Update the variables in the `.env` file as needed.

3.  **Build and run the application with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4.  **Access the application:**
    -   **Frontend:** [http://localhost:3000](http://localhost:3000)
    -   **Backend API:** [http://localhost:8000/docs](http://localhost:8000/docs)

## Deploying to Render

This project is configured for easy deployment to [Render](https://render.com/) using a `render.yaml` Blueprint.

1.  **Create a new Blueprint Instance on Render.**
2.  **Connect your GitHub account and select the repository.**
3.  **Copy and paste the contents of `TaskPilot/render.yaml` into the Blueprint editor.**
4.  **Create a new Environment Group** named `taskpilot-secrets` to store your environment variables (e.g., API keys, `SECRET_KEY`).
5.  **Click "Apply" to deploy the services.**

Render will automatically provision and deploy the Redis instance, backend, frontend, and Celery workers based on the Blueprint configuration.