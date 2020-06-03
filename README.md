# exampleFlaskDeployment
build docker container locally

docker build . -t flask-server:latest

docker run -d --name flask-server -p 80:80 flask-server

Afterwards is the flaskserver is reachable at 0.0.0.0:80

or the docker container could be deployed via docker-compose