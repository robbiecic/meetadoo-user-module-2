# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Connec to gcloud
sh .circleci/gcloud.sh

# Push docker to gcloud container registry tagged by the Git Hash value
echo "Ready to deploy to GCP ... "

# Create compute instance from the image correspdonding to this build
# gcloud compute instances create-with-container meetadoo-user-api-instance \
#      --container-image 'gcr.io/meetadoo/'"${IMAGE_NAME}"':'"$CIRCLE_SHA1"'"'

# Once instance has been created, when need to run update instead
gcloud compute instances update-container meetadoo-user-api-instance \
    --container-image 'gcr.io/meetadoo/'"${IMAGE_NAME}"':'"$CIRCLE_SHA1"'"'

# To change machine type, run these commands
# gcloud compute instances stop meetadoo-user-api-instance
# gcloud compute instances set-machine-type meetadoo-user-api-instance \
#     --zone ${GOOGLE_COMPUTE_ZONE} --machine-type f1-micro
# gcloud compute instances start meetadoo-user-api-instance
