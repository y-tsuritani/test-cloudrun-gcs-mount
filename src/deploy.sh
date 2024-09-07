docker build -t gcr.io/any-development/gcs-volume-mount-dev .

docker push gcr.io/any-development/gcs-volume-mount-dev

gcloud run deploy gcs-volume-mount-dev \
  --image=gcr.io/any-development/gcs-volume-mount-dev \
  --region=us-central1 \
  --allow-unauthenticated \
  --add-volume-mount=[volume=gcs-volume, mount-path=/gcs] \
  --add-volume=[name=gcs-volume, type=cloud-storage, bucket=test-gcs-vol-mount]