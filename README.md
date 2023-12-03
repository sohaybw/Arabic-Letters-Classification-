# Arabic Letters Classification API using FastAPI

This API is designed to classify Arabic letters provided in image format. It utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.


## Table of content

- [FastAPI Arabicletters](#fastapi-arabic_letters_classifier)
  - [Table of content](#table-of-content)
  - [Overview](#overview)
  -[Model Training](#Model-Training)
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

## Model-Training

For those interested in understanding how the Arabic letters classification model was trained, a Jupyter notebook is provided in the `model_training` directory. Follow the steps below to utilize the notebook:

### Model Training Notebook

- Navigate to the [notebooks](./api/src/notebooks) directory.
- Open the `Arabic_Letters_Classification_Model_Training.ipynb` notebook using Jupyter or any compatible environment.
- The notebook provides detailed steps for:
  - Data pre-processing.
  - Model architecture selection and setup.
  - Training the model on the Arabic letters dataset.
  - Evaluating the model's performance.
  - Saving the trained model weights.

Feel free to experiment with different architectures, hyperparameters, or datasets to improve the model's accuracy or adapt it to your specific use case. Remember to update the API with the new trained model if you achieve better results.
## Model WEIGHTS 
- https://drive.google.com/drive/folders/1x3CFRf90V6FbI-L0ayx5FhDv6U_ltNm8?usp=sharing
-Kindly Download Model Weights from above link and put it in (./api/src/static)
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
