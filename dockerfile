# Use uwsgi-nginx-flask-python3.6 as parent image
FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

# default port for this image is port 80

# overrides the initial main.py from the image
RUN mv /app/app.py /app/main.py

RUN pip3 install -r requirements.txt