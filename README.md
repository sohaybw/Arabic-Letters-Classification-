# Arabic Letters Classification API using FastAPI

This API is designed to classify Arabic letters provided in image format. It utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.


## Table of content

- [FastAPI boilerplate](#fastapi-arabic_letters_classifier)
  - [Table of content](#table-of-content)
  - [Overview](#overview)
  - [Development](#development)
    - [Prerequisites](#prerequisites)
    - [Configuration](#configuration)
    - [Run instructions](#run-instructions)
  - [Docker instructions](#docker-instructions)
    - [For Production](#for-production)
      - [Build image](#build-image)
      - [Publish image](#publish-image)
      - [Test it](#test-it)
  - [API Details](#api-details)


## Overview

The goal of this API is to provide a simple yet effective method to classify Arabic letters found in images. It serves as a convenient tool for developers and researchers working on projects involving Arabic character recognition or classification.


## Development

### Prerequisites

- Python v3.10

### Configuration

- Copy [`example.dev.env`](example.dev.env) to `dev.env`

- Adapt `dev.env`

### Run instructions

- Create a virtual environment and install dependencies

```sh
cd api
pip install virtualenv
virtualenv ./env
source env/bin/activate
pip install -r requirements.txt
```

- Load env variables

```sh
# For windows
set -a && source ../dev.env && set +a

# For linux
source dev.env
```

- Start the server

```sh
python src/main.py
```

- Lint src dir

```sh
flake8 src
```

## Docker instructions

### For Production

- Copy [example.env](example.env) to .env file and adapt you variables [See configuration section](#configuration)

#### Build image

```sh
make build
```

#### Publish image

```sh
make publish
```

#### Test it

```sh
docker-compose -f docker-compose.yml up -d
```

## API Details

- [API Details](./api/README.md)
