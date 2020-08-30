FROM python:3.8-alpine as baseimage
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR app
COPY . .

FROM baseimage as runtimeimage

EXPOSE 5000
CMD python3 main.py
