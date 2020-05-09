# !/bin/bash
echo "Building docker image... \n"
docker build --rm=false -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 .
echo "Exporting environment variable to json file... \n"
echo $GCLOUD_SERVICE_KEY | iconv -t utf-8 > ${HOME}/gcloud-service-key1.json
echo "Replacing special characters to convert back to valid json... \n"
sed -E ':a;N;$!ba;s/\r{0,1}\n/\\n/g' ${HOME}/gcloud-service-key1.json > ${HOME}/gcloud-service-key.json
echo "\n Attempting to authenticated to gcloud ... \n"
gcloud auth activate-service-account --key-file=${HOME}/gcloud-service-key.json
gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}
echo "Pushing docker image to Google Cloud Container Registry... \n"
gcloud docker -- push gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1
