FROM python:3.8-alpine AS baseimage

WORKDIR app

RUN pip install -r requirements.txt

FROM baseimage AS runtimeimage

#ENV FLASK_APP=main.py
#ENV FLASK_ENV=development
EXPOSE 5000
CMD python3 main.py
