gcloud run deploy gcs-volume-mount-dev \
  --source=./src \
  --region=us-central1 \
  --allow-unauthenticated \
  --service-account test-run-gcs-mount \
  --add-volume=name=gcs-volume,type=cloud-storage,bucket=test-gcs-vol-mount \
  --add-volume-mount=volume=gcs-volume,mount-path=/mnt/gcs \
  --update-env-vars=MOUNT_PATH=/mnt/gcs,PROJECT_ID=any-development,TABLE_NAME=users,SOURCE_DATASET=TEST_DATA \
  --memory=3Gi
