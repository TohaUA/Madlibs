# Base image
FROM python:3.9

# Install pipenv
RUN pip install pipenv

# Docker work directory
WORKDIR /code

# Install Python depedencies
COPY Pipfile.lock Pipfile.lock

RUN pipenv sync --bare

# Copy our application source code
COPY ./app /code/app

# Startup command
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
