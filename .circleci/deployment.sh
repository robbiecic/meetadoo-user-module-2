# !/bin/bash
# docker build --rm=false -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 .
echo $GCLOUD_SERVICE_KEY > ${HOME}/gcloud-service-key1.json
cat ${HOME}/gcloud-service-key1.json
sed $'s/[^[:print:]\t]//g' ${HOME}/gcloud-service-key1.json > ${HOME}/gcloud-service-key.json
cat ${HOME}/gcloud-service-key.json
echo "\n Attempting to authenticated to gcloud ... \n"
gcloud auth activate-service-account --key-file=${HOME}/gcloud-service-key.json
gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
gcloud --quiet config set compute/zone ${GOOGLE_COMPUTE_ZONE}
# gcloud docker push gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1
