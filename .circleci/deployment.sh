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
# kubectl apply --validate=true -f k8s/

echo '{"spec":{"template":{"spec":{"containers":[{"name":"meetadoo-user-api","image":"gcr.io/meetadoo/'"${IMAGE_NAME}"':'"$CIRCLE_SHA1"'"}]}}}}'

 # The K8s deployment intelligently upgrades the cluster by shutting down old containers and starting up-to-date ones.
kubectl patch deployment meetadoo-user-api -p '{"spec":{"template":{"spec":{"containers":[{"name":"meetadoo-user-api","image":"gcr.io/meetadoo/'"${IMAGE_NAME}""':'"$CIRCLE_SHA1"'"}]}}}}'
