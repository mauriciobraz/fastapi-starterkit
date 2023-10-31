# FastAPI StarterKit

FastAPI StarterKit serves as a comprehensive boilerplate for FastAPI applications, incorporating best practices for RESTful API development, error handling, code organization, and task automation. The project is equipped with a pre-configured Continuous Integration (CI) setup using GitHub Actions and development settings for Visual Studio Code (VSCode).

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
    docker build -t fastapi-starterkit .
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -p 8000:8000 fastapi-starterkit
    ```

## Deployment

Production deployments are streamlined through a Docker Compose setup, orchestrated via a `deploy` target in the Makefile. This setup ensures that both the FastAPI application and the Caddy server are built and run in a Dockerized environment, providing a level of isolation and consistency across deployments.

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
   - Ensures that the Caddy server automatically provisions SSL/TLS certificates for secure HTTPS connections.

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
    make deploy
    ```

### Troubleshooting

If you encounter issues during the deployment process, check the logs of the Docker containers for any error messages:

```bash
docker-compose logs
```

You can also inspect individual containers for more detailed information:

```bash
docker inspect <container_name>
```

## Continuous Integration (CI)

The project uses GitHub Actions to run a Continuous Integration pipeline on every `push`, `pull_request`, and `workflow_dispatch` event. The pipeline performs the following tasks:

1. **Checks out the code**: Uses the GitHub `actions/checkout` action.
2. **Sets up Python**: Configures the Python version based on `.python-version`.
3. **Caches Dependencies**: Utilizes GitHub's cache action for both Poetry and Python packages.
4. **Installs Poetry**: Downloads and installs Poetry.
5. **Installs Dependencies**: Uses `make install` to install project dependencies.
6. **Lint and Format Check**: Runs lint checks with `make lint`.
7. **Run Tests**: Executes the unit tests using `make test`.

For more details, refer to the [CI configuration file](./.github/workflows/ci.yml).

## VSCode Settings

The repository includes a pre-configured `.vscode` folder containing settings for a consistent development environment. These settings are especially helpful if you are using Visual Studio Code as your IDE.

## Makefile Commands

- `make help`: Display help information.
- `make install`: Install project dependencies.
- `make fmt`: Format the code.
- `make lint`: Run lint checks.
- `make test`: Run tests.
- `make clean`: Clean the project directory.
- `make venv`: Set up a virtual environment.

## Testing

To execute unit tests, use the following command:

```bash
make test
```

## Project Structure

```plaintext
├── Dockerfile
├── LICENSE
├── Makefile
├── mypy.ini
├── poetry.lock
├── pyproject.toml
├── README.md
├── source
│   └── ...
└── tests
    └── ...
```

## Administrative Files

- **CODEOWNERS**: You'll need to update or delete the `CODEOWNERS` file under the `.github` folder to specify the new owners or maintainers of the repository.
- **FUNDING.yml**: Similarly, update or remove the `FUNDING.yml` file under the `.github` folder, depending on your project's funding settings.

## License

FastAPI StarterKit is licensed under the terms of the [MIT License](LICENSE).
