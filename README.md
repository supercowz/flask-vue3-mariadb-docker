# Overview
A starter project for a basic web application.

Vue3 frontend with a Flask API backend with a MariaDB.

Everything is dockerized and ready for production.

# Setup

## Setup the initial values

1. ```python3 setup.py```

## Install dependencies:

1. ```cd api && python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```flask db migrate```
4. ```deactivate```
4. ```cd ..```
5. ```cd web && npm install```

## Setup the database:

1. ```docker-compose build app-db```
2. ```docker-compose up -d app-db```

## Run the application:
Open two terminal windows.

First window:

```cd api```

```source venv/bin/activate```

```flask run```

Second window:

```cd web```

```npm start```