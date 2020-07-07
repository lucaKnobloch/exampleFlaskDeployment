# Example - Flask - Server
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lucaKnobloch_exampleFlaskDeployment&metric=alert_status)](https://sonarcloud.io/dashboard?id=lucaKnobloch_exampleFlaskDeployment)
## Build Docker Locally 

  `docker build . -t flask-server:latest`

The created image is executable with the following command: 
  
  `docker run -d --name flask-server -p 80:80 flask-server`

  Afterwards is the flask-server is reachable at
     `127.0.0.1:80`

### Two scenarios can be used to test the services 
1. 127.0.0.1:80/ -> will return "Hello World from Flask" 
2. 127.0.0.1:80/books -> will return a list of books in the json format 

## Deployment
The docker container needs to be created afterwards could be the docker-compose be used to deploy it.

