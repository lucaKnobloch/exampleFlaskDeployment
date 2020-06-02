# Use uwsgi-nginx-flask-python3.7 as parent image
FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY . /app

# overrides the initial main.py from the image
RUN mv /app/app.py /app/main.py

RUN pip3 install -r requirements.txt