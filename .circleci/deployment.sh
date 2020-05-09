# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

# Create an intuitive tag with the current date appending with the CirclCi build number
echo "Creating build version number..."
DATE=$(date +'%Y.%m.%d')
VERSION=$DATE.$CIRCLE_BUILD_NUM
echo "This build version is " $VERSION "\n"

# Build and tag docker image
echo "Building docker image... \n"
docker build --rm=false -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$VERSION .

# Pull gcloud credentials from environmental variable
echo "Exporting environment variable to json file... \n"
echo $GCLOUD_SERVICE_KEY | iconv -t utf-8 > ${HOME}/gcloud-service-key1.json
echo "Replacing special characters to convert back to valid json... \n"
sed -E ':a;N;$!ba;s/\r{0,1}\n/\\n/g' ${HOME}/gcloud-service-key1.json > ${HOME}/gcloud-service-key.json

# Authenticate to gcloud container registry
echo "\n Attempting to authenticated to gcloud ... \n"
gcloud auth activate-service-account --key-file=${HOME}/gcloud-service-key.json
gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}

# Finally, push docker to gcloud container registry
echo "Pushing docker image to Google Cloud Container Registry... \n"
gcloud docker -- push gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}
