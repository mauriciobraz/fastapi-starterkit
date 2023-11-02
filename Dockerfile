# Use an official Python runtime as a parent image
FROM python:3.10.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# Copy only the project metadata files
COPY pyproject.toml poetry.lock /app/

# Install dependencies with Poetry
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the source code
COPY . /app/

# Expose the port
EXPOSE 8000

# Set environment variables
ENV ENVIRONMENT=production

# Run the application
CMD ["poetry", "run", "start"]
