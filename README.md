# FastAPI StarterKit

## Installation

### Prerequisites for Development

- Python 3.10.11
- [Poetry](https://python-poetry.org/) for dependency management
- [Docker](https://www.docker.com/) (optional)

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mauriciobraz/fastapi-starterkit.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd fastapi-starterkit
    ```

3. **Install Dependencies:**

    ```bash
    make install
    ```

## Running the Application

### Using Uvicorn

Run the FastAPI application using the following command:

```bash
uvicorn source.main:app --reload
```

### Using Docker

1. **Build the Docker Image:**

    ```bash
    docker build -t fastapi-starterkit docker/Poetry.dockerfile
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -p 8000:8000 fastapi-starterkit
    ```

## Deployment

Production deployments are handled by Docker Compose, orchestrated via a `deploy` target in the Makefile. This setup ensures that both the FastAPI application and the Caddy server are built and run in a Dockerized environment, providing a level of isolation and consistency across deployments.

### Prerequisites for Deployment

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on the deployment machine.
- A `Caddyfile` and `docker-compose.yml` file configured for your production environment.

### Deployment Steps

1. **Pull the Latest Code:**

   Ensure you have the latest codebase with all the necessary configurations:

    ```bash
    git pull origin main
    ```

2. **Build and Deploy:**

   Utilize the `deploy` target in the Makefile to build the Docker images and run the containers:

    ```bash
    make deploy
    ```

   This command performs the following actions:

   - Builds the Docker images for the FastAPI application and the Caddy server as defined in the `docker-compose.yml` file.
   - Runs the containers in detached mode, allowing them to run in the background.
   - Sets up a network for the containers to communicate with each other.
   - Ensures that the Caddy server automatically provisions SSL/TLS certificates for secure HTTPS connections, given that valid DNS records are set and an email is provided for certificate management. Check [Caddy's automatic HTTPS documentation](https://caddyserver.com/docs/automatic-https#dns-challenge) for more details on DNS challenges.

   Please note that the Docker images may take between 30 seconds to 1 minute to fully load. Initially, the Caddy server will load faster, possibly displaying `502: no upstreams available` indicating no upstreams were found. This is a transient state while the FastAPI application is still loading; waiting for a brief period should resolve this issue and show the application running as expected.

3. **Verify Deployment:**

   After running the `make deploy` command, verify the deployment by navigating to your domain in a web browser:

    ```plaintext
    https://yourdomain.com
    ```

   You should see your FastAPI application running, secured with HTTPS.

### Updating the Deployment

To update the deployment with new code or configurations:

1. **Pull the Latest Code:**

    ```bash
    git pull origin main
    ```

2. **Re-Deploy:**

    ```bash
    # Recreate the containers, volumes, and networks.
    make deploy

    # Without recreating the containers, volumes, and networks.
    docker-compose up -d
    ```

## Makefile Commands

- `make test`: Run tests.
- `make fmt`: Format the code.
- `make lint`: Run lint checks.
- `make help`: Display help information.
- `make venv`: Set up a virtual environment.
- `make clean`: Clean the project directory.
- `make install`: Install project dependencies.

## Code Quality and Linting

This project enforces code quality and consistency using a combination of tools. Below are the tools used and the commands to run them:

- **Flake8** for checking code base against coding style (PEP 8), `make lint`.
- **Mypy** for optional static typing, `make type`.
- **Black** for code formatting, `make fmt`.
- **Pytest** for running tests, `make test`.

Each of these tools is configured with sensible defaults to ensure code quality while minimizing configuration overhead.

## VSCode Settings

The repository includes a pre-configured `.vscode` folder containing settings for a consistent development environment. These settings are especially helpful if you are using Visual Studio Code as your IDE.

## Continuous Integration (CI) with GitHub Actions

The repository is pre-configured with a GitHub Actions workflow for Continuous Integration, ensuring code consistency and quality. Refer to [CI configuration file](./.github/workflows/ci.yml) for more details.

## Utility File Helpers

A set of pre-built utility file helpers is included to simplify common tasks and keep the codebase DRY (Don't Repeat Yourself). They can be found in the `utils` directory within the project structure.
