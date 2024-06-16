# Overview
CBTODO

# Setup

## Install dependencies:

1. ```cd api && python3 -m venv venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```deactivate```
4. ```cd ..```
5. ```cd web && npm install```

## Setup the database:

1. ```docker-compose build app-db```
2. ```docker-compose up -d app-db```

## Run the application:

1. Open two terminal windows
2. In the first terminal window, run: ```cd api && source venv/bin/activate && flask run```
3. In the second terminal window, run: ```cd web && npm start```