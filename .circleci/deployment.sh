# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Connec to gcloud
.circleci/gcloud.sh

# Push docker to gcloud container registry tagged by the Git Hash value
echo "Ready to deploy to GKE ... "
