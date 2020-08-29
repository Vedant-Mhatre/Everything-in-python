FROM python:3.8-alpine
ADD . /todo
WORKDIR /todo
#RUN sudo apt-get install python3-pip
#RUN python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip
RUN pip install -r requirements.txt
