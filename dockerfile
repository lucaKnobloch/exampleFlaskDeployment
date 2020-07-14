# Use uwsgi-nginx-flask-python3.6 as parent image
FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

# the EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime.
# default port for this image is port 80
# for custom port enable the following commands
# ENV LISTEN_PORT 8080
# EXPOSE 8080

# overrides the initial main.py from the image
RUN mv /app/app.py /app/main.py

RUN pip3 install -r requirements.txt