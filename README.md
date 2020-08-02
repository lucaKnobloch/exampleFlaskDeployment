# Example - Flask - Server

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lucaKnobloch_exampleFlaskDeployment&metric=alert_status)](https://sonarcloud.io/dashboard?id=lucaKnobloch_exampleFlaskDeployment)

Its a baseline of a flask server which can be easily extended to the personal needs. The parent image included an uwsgi and nginx in combination with flask. It is published by Tiangolog and can be found here https://github.com/tiangolo/uwsgi-nginx-flask-docker

## Build and Run Docker Locally 

#### Install Command
  `docker build . -t flask-server:latest`

#### Run Command
The created image is executable with the following command: 
  
  `docker run -d --name flask-server -p 5000:80 flask-server`
  
  The default settings expose the image on port 80 and will be published to port 5000. If you want to redirect it, you can do it either there or in the docker-compose file.

  Afterward is the flask-server is reachable at
     `127.0.0.1:5000`

### Test Cases
Two scenarios can be used to test the services 
1. 127.0.0.1:5000/ -> will return "Hello World from Flask" 
2. 127.0.0.1:5000/books -> will return a list of books in the json format 

### Deployment
The docker container needs to be created first to be deployable with the docker-compose.
