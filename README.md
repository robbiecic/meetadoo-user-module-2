## Summary

Build a cloud-agnostic API with python to replace the AWS-native API already running.

## Commands

- docker build -t meetadoo-user-api:latest .
- docker run -d --env-file env.list -p 5000:5000 meetadoo-user-api
- docker container ls
- docker stop <container id>

## api

/swagger-ui
