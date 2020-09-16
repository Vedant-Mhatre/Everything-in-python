# Mongo Flask

## About
The goal of this project is to build a simple implementation for connecting mongodb to flask application and deployment using docker

## Getting Started

### Prerequisites
* Docker
* Docker-compose

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

cd Everything-in-python/Web/Mongo-Flask
```

3. Build the container according to desired configuration.

```
docker-compose build

db uses an image, skipping
Building web
Step 1/5 : FROM python:3.8-alpine
 ---> 44fceb565b2a
Step 2/5 : RUN pip install flask
 ---> Running in 7b3f329994bc
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1.tar.gz (19 kB)
Building wheels for collected packages: MarkupSafe
  Building wheel for MarkupSafe (setup.py): started
  Building wheel for MarkupSafe (setup.py): finished with status 'done'
  Created wheel for MarkupSafe: filename=MarkupSafe-1.1.1-py3-none-any.whl size=12629 sha256=2de6c944e753a707b691683d3f5aa17d573149b268a3f81df3abc956323aa90e
  Stored in directory: /root/.cache/pip/wheels/0c/61/d6/4db4f4c28254856e82305fdb1f752ed7f8482e54c384d8cb0e
Successfully built MarkupSafe
Installing collected packages: itsdangerous, click, Werkzeug, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
WARNING: You are using pip version 20.2.2; however, version 20.2.3 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Removing intermediate container 7b3f329994bc
 ---> ca2487478591
Step 3/5 : RUN pip install pymongo
 ---> Running in c87b184e562c
Collecting pymongo
  Downloading pymongo-3.11.0.tar.gz (771 kB)
Building wheels for collected packages: pymongo
  Building wheel for pymongo (setup.py): started
  Building wheel for pymongo (setup.py): finished with status 'done'
  Created wheel for pymongo: filename=pymongo-3.11.0-cp38-cp38-linux_x86_64.whl size=344187 sha256=89dbfc94a291c917a5c1de630497080efff6029fdbb48508706c22ed40783783
  Stored in directory: /root/.cache/pip/wheels/c1/92/e4/bc715566019670eb238a8b6e698d30ce013af76be1ecde9c9b
Successfully built pymongo
Installing collected packages: pymongo
Successfully installed pymongo-3.11.0
WARNING: You are using pip version 20.2.2; however, version 20.2.3 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Removing intermediate container c87b184e562c
 ---> 753180f89fae
Step 4/5 : ADD . /todo
 ---> 62b5988bd3ca
Step 5/5 : WORKDIR /todo
 ---> Running in cabf0d869033
Removing intermediate container cabf0d869033
 ---> f3b3dc8dcce2
Successfully built f3b3dc8dcce2
Successfully tagged mongo-flask_web:latest

```

## Deployment
Easy Deployment using only 1 Step

1. Start container
```
docker-compose up

Creating mongo-flask_db_1 ... done
Creating mongo-flask_web_1 ... done
Attaching to mongo-flask_db_1, mongo-flask_web_1
db_1   | 2020-09-11T10:34:08.105+0000 I JOURNAL  [initandlisten] journal dir=/data/db/journal
db_1   | 2020-09-11T10:34:08.109+0000 I JOURNAL  [initandlisten] recover : no journal files present, no recovery needed
web_1  |  * Serving Flask app "app" (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |    Use a production WSGI server instead.
web_1  |  * Debug mode: on
web_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1  |  * Restarting with stat
web_1  |  * Debugger is active!
web_1  |  * Debugger PIN: 749-702-492

```

## To Do
- [ ] Use latest mongodb image
- [ ] Use yaml version 3
- [ ] Add documentation

## Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) Flask is a micro web framework written in Python
* [pymongo](https://pymongo.readthedocs.io/en/stable/) Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.
