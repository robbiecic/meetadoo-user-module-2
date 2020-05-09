# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Build and tag docker image
echo "Building docker image... \n"
docker build --rm=false -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 .

# Connec to gcloud
./gcloush.sh

# Push docker to gcloud container registry tagged by the Git Hash value
echo "Pushing docker image to Google Cloud Container Registry... \n"
gcloud docker -- push gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1

# Create an intuitive tag with the current date appending with the CirclCi build number
echo "Creating build version number..."
DATE=$(date +'%Y.%m.%d')
VERSION=$DATE.$CIRCLE_BUILD_NUM
echo "This build version is " $VERSION "\n"

# Tag image with build versoin
gcloud container images add-tag gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$VERSION
