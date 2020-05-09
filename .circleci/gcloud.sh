# !/bin/bash
# Set -e ensures errors aren't surpressed and traverse to circleci caller
set -e

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
