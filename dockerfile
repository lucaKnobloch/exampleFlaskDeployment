# Use uwsgi-nginx-flask-python3.7 as parent image
FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY . /app

#the EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime.
#You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified
#EXPOSE 80

# overrides the initial main.py from the image
RUN mv /app/app.py /app/main.py

RUN pip3 install -r requirements.txt