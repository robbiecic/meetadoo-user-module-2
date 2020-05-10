## Summary

Build a cloud-agnostic API with python to replace the AWS-native API already running.

## Commands

- start local kubernetes `minkube start`
- In local sessions you must run `eval $(minikube docker-env)` in the terminal first, then build the docker image and run the kubectl commands
- `docker build -t meetadoo-user-api:latest .`
- `docker run -d --env-file env.list -p 5000:5000 meetadoo-user-api`
- `docker container ls`
- `docker stop <container id>`

## api

/swagger-ui

## Kubernets deployment commands

- `kubectl create -f k8s/manifest.yaml`
- `kubectl expose deployment meetadoo-user-api --type="LoadBalancer" --port=80`
- Makes kubenetes cluster available through minikube: `minikube service meetadoo-user-api-service`
- Updates deployment: `kubectl apply -f k8s/manifest.yaml`
- Updates service: `kubectl apply -f k8s/service.yaml`
- Shows resources available on kubernetes cluster: `kubectl describe node`
