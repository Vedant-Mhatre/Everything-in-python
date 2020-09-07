# Insta Flask

## About
The goal of this project is to build a simple implementation of Instagram REST apis using flask for beginner's to learn.
MongoDB will be used as database and deployment using docker

## Getting Started

### Prerequisites
* Docker
* Docker-compose
docker-compose file builds an image using the Dockerfile inside app directory, pulls mongodb image and links them together.

### Installing

Get the project up and running locally in just 3 easy steps.

1. Create a personal Fork of this repository.

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/your_username/Everything-in-python.git

Cloning into 'Everything-in-python'...
remote: Enumerating objects: 113, done.
remote: Counting objects: 100% (113/113), done.
remote: Compressing objects: 100% (80/80), done.
Receiving objects: 100% (2845/2845), 12.52 MiB | 5.21 MiB/s, done.

cd Everything-in-python/REST\ APIs/insta_flask
```

3. Build the container according to desired configuration.
 Docker-compose file builds an image using the Dockerfile inside app directory, pulls mongodb image and links them together.

```
docker-compose build

db uses an image, skipping
Building app
Step 1/8 : FROM python:3.8-alpine as baseimage
 ---> 44fceb565b2a
Step 2/8 : COPY requirements.txt .
 ---> Using cache
 ---> 508a70374762
Step 3/8 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> ebb8b47871a1
Step 4/8 : WORKDIR app
 ---> Using cache
 ---> e218daf67bb5
Step 5/8 : COPY . .
 ---> 06d366e573d7
Step 6/8 : FROM baseimage as runtimeimage
 ---> 06d366e573d7
Step 7/8 : EXPOSE 5000
 ---> Running in d069ede5dc33
Removing intermediate container d069ede5dc33
 ---> aeee61a93426
Step 8/8 : CMD python3 main.py
 ---> Running in e926439dc875
Removing intermediate container e926439dc875
 ---> c039f50dcd09
Successfully built c039f50dcd09
Successfully tagged insta_flask_app:latest
```

## Deployment
Easy Deployment using only 1 Step

1. Start container
```
docker-compose up

Starting insta_flask_db_1 ... done
Recreating insta_flask_app_1 ... done
Attaching to insta_flask_db_1, insta_flask_app_1
db_1   | 2020-09-07T18:08:55.507+0000 I JOURNAL  [initandlisten] journal dir=/data/db/journal
db_1   | 2020-09-07T18:08:55.552+0000 I JOURNAL  [initandlisten] recover : no journal files present, no recovery needed
db_1   | 2020-09-07T18:08:56.231+0000 I JOURNAL  [durability] Durability thread started
db_1   | 2020-09-07T18:08:56.232+0000 I JOURNAL  [journal writer] Journal writer thread started
db_1   | 2020-09-07T18:08:56.409+0000 I CONTROL  [initandlisten] MongoDB starting : pid=1 port=27017 dbpath=/data/db 64-bit host=3be68abe3890
db_1   | 2020-09-07T18:08:56.410+0000 I CONTROL  [initandlisten] db version v3.0.2
db_1   | 2020-09-07T18:08:56.410+0000 I CONTROL  [initandlisten] git version: 6201872043ecbbc0a4cc169b5482dcf385fc464f
db_1   | 2020-09-07T18:08:56.410+0000 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1e 11 Feb 2013
db_1   | 2020-09-07T18:08:56.411+0000 I CONTROL  [initandlisten] build info: Linux ip-10-171-120-232 3.2.0-4-amd64 #1 SMP Debian 3.2.46-1 x86_64 BOOST_LIB_VERSION=1_49
db_1   | 2020-09-07T18:08:56.411+0000 I CONTROL  [initandlisten] allocator: tcmalloc
db_1   | 2020-09-07T18:08:56.411+0000 I CONTROL  [initandlisten] options: {}
db_1   | 2020-09-07T18:08:59.909+0000 I NETWORK  [initandlisten] waiting for connections on port 27017
app_1  |  * Serving Flask app "main" (lazy loading)
app_1  |  * Environment: production
app_1  |    WARNING: This is a development server. Do not use it in a production deployment.
app_1  |    Use a production WSGI server instead.
app_1  |  * Debug mode: on
db_1   | 2020-09-07T18:09:00.483+0000 I NETWORK  [initandlisten] connection accepted from 172.17.0.3:34268 #1 (1 connection now open)
app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
app_1  |  * Restarting with stat
db_1   | 2020-09-07T18:09:00.971+0000 I NETWORK  [initandlisten] connection accepted from 172.17.0.3:34270 #2 (2 connections now open)
app_1  |  * Debugger is active!
app_1  |  * Debugger PIN: 188-908-057
```

## Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) Flask is a micro web framework written in Python
* [flask_restful](https://flask-restful.readthedocs.io/en/latest/) An extension for Flask that adds support for quickly building REST APIs.
* [requests](https://requests.readthedocs.io/en/master/) Simple HTTP library for Python
* [pymongo](https://pymongo.readthedocs.io/en/stable/) Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.
