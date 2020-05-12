# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Connec to gcloud
sh .circleci/gcloud.sh

# Push docker to gcloud container registry tagged by the Git Hash value
echo "Ready to deploy to GKE ... "

# Generate kubeconfig to access cluster
gcloud container clusters get-credentials user-api-cluster --zone=us-central1-c

# Check current context
kubectl config current-context

# Dry run applying kubernetes settings all manifests in the k8s folder
kubectl apply --validate=true --dry-run=true -f k8s/

# Apply all manifests
kubectl apply --validate=true -f k8s/


# kubectl create deployment hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1
# kubectl expose deployment hello-web --type=LoadBalancer --port 80 --target-port 8080
