# !/bin/bash

set -e

echo "Deploying"

echo $ACCOUNT_KEY > ${HOME}/gcloud-service-key.json

gcloud auth activate-service-account ${ACCOUNT_ID} --key-file ${HOME}/gcloud-service-key.json

gcloud config set project coding-dojo-251421

gcloud --quiet config set container/cluster coding-dojo

gcloud config set compute/zone us-central1-a

gcloud --quiet container clusters get-credentials coding-dojo-andresg

docker build -t gcr.io/coding-dojo-251421/coding-dojo:$CIRCLE_SHA1 .

gcloud docker -- push gcr.io/coding-dojo-251421/coding-dojo:$CIRCLE_SHA1

kubectl set image deployment/coding-dojo-andresg coding-dojo=gcr.io/coding-dojo-251421/coding-dojo:$CIRCLE_SHA1

echo " Successfully deployed"
