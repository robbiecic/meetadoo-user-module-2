# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Connec to gcloud
sh .circleci/gcloud.sh

# Push docker to gcloud container registry tagged by the Git Hash value
echo "Ready to deploy to GKE ... "
# kubectl create deployment hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1
# kubectl expose deployment hello-web --type=LoadBalancer --port 80 --target-port 8080
