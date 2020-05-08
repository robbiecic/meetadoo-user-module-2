# !/bin/bash
echo ${GCLOUD_SERVICE_KEY} > base64 --decode --ignore-garbage > ${HOME}/gcp-key.json
docker build --rm=false -t gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1 .
cat ${HOME}/gcp-key.json
gcloud auth activate-service-account --key-file ${HOME}/gcp-key.json
gcloud --quiet config set project ${GOOGLE_PROJECT_ID}
gcloud docker -- push gcr.io/${GOOGLE_PROJECT_ID}/${IMAGE_NAME}:$CIRCLE_SHA1
