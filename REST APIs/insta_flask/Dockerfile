FROM python:3.8-alpine AS baseimage
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . .

FROM baseimage AS runtimeimage

#ENV FLASK_APP=main.py
#ENV FLASK_ENV=development
CMD python3 main.py
