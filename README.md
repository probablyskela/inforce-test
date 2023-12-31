# Inforce python task

# [API reference](docs/README.md)

## Use flake8
```sh
flake8 inforce
```

## Setup

### Create virtual environment
```sh
python -m venv .venv
```

### Activate virtual environment and install requirements
```sh
source .venv/bin/activate
pip install -r requirements.txt
```

### Run application
```sh
python manage.py runserver 0.0.0.0:8000
```

## Setup (docker containers)

### Run docker compose
```sh
docker compose up --build -d
```


## Run tests with

```sh
pytest
```

Or in docker containers

```sh
docker compose up --build -d
docker compose exec server pytest
```