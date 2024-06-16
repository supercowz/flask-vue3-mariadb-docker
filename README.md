# Overview
A starter project for a basic web application with a user login and registration system and basic styling.

Vue3 frontend with a Flask API backend with a MariaDB.

For CSS styling, there is a lightweight boilerplate I use called [Skeleton](http://getskeleton.com/)

Everything is dockerized and ready for production.

# Setup

## Setup the initial values

1. ```python3 setup.py```

## Setup the database:

1. ```docker-compose build app-db```
2. ```docker-compose up -d app-db```

## Install dependencies:

1. ```cd api && python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```flask db migrate```
4. ```deactivate```
4. ```cd ..```
5. ```cd web && npm install```

## Run the application:
Open two terminal windows.

First window:

```cd api```

```source venv/bin/activate```

```flask run```

Second window:

```cd web```

```npm start```