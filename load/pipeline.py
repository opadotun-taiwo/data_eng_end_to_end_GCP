# pipeline.py

import os
import requests
import logging
import dlt
from google.cloud import storage
from dlt.sources.filesystem import filesystem, read_parquet
from dlt.sources import incremental

# =====================================================
# CONFIG
# =====================================================

PROJECT_ID = "gothic-sled-453213-i2"
BUCKET_NAME = "gothic-sled-453213-i2-trips-bucket"
DOWNLOAD_DIR = "temp_downloads"
GCS_PREFIX = "rides_dataset/"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

client = storage.Client(project=PROJECT_ID)
bucket = client.bucket(BUCKET_NAME)

# =====================================================
# HELPERS
# =====================================================

def blob_exists(blob_name):
    blob = bucket.blob(blob_name)
    return blob.exists()

def download_file(url, local_path):
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

def upload_file(local_path, blob_name):
    blob = bucket.blob(blob_name)
    blob.chunk_size = 10 * 1024 * 1024  # 10MB chunks
    blob.upload_from_filename(local_path, timeout=600)

# =====================================================
# STEP 1 — DOWNLOAD + UPLOAD (IDEMPOTENT)
# =====================================================

prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
taxi_types = ["yellow", "green"]

for taxi in taxi_types:
    for month in range(1, 6):

        file_name = f"{taxi}_tripdata_2024-{month:02d}.parquet"
        blob_name = GCS_PREFIX + file_name
        local_path = os.path.join(DOWNLOAD_DIR, file_name)
        url = prefix + file_name

        # Skip if already uploaded
        if blob_exists(blob_name):
            print(f"Already in GCS, skipping: {file_name}")
            continue

        # Download only if not local
        if not os.path.exists(local_path):
            print(f"Downloading {file_name}...")
            download_file(url, local_path)
        else:
            print(f"Already downloaded locally: {file_name}")

        print(f"Uploading {file_name} to GCS...")
        upload_file(local_path, blob_name)

        os.remove(local_path)
        print(f"Cleaned up local file: {file_name}")

# Upload finance file (idempotent)
finance_file = r"C:\Users\admin\Desktop\complete_data_project\trips\load\customer_data.csv"
finance_blob = GCS_PREFIX + "customer_data.csv"

if not blob_exists(finance_blob):
    print("Uploading finance file...")
    upload_file(finance_file, finance_blob)
else:
    print("Finance file already exists.")

print("Step 1 complete.")

# ... (Keep your Step 1 code as is)

# =====================================================
# STEP 2 — LOAD FROM GCS TO BIGQUERY (OPTIMIZED)
# =====================================================
logging.basicConfig(level=logging.INFO)

@dlt.source(name="gcs_rides")
def taxi_data():

    bucket_url = f"gs://{BUCKET_NAME}"

    # Yellow taxi files
    yellow = (
        filesystem(bucket_url, file_glob="rides_dataset/yellow_tripdata_*.parquet")
        | read_parquet()
    )

    yield yellow.with_name("yellow_trips")

    # Green taxi files
    green = (
        filesystem(bucket_url, file_glob="rides_dataset/green_tripdata_*.parquet")
        | read_parquet()
    )

    yield green.with_name("green_trips")


pipeline = dlt.pipeline(
    pipeline_name="nyc_taxi_pipeline",
    destination="bigquery",
    dataset_name="trips_dataset",
)

try:
    load_info = pipeline.run(
        taxi_data(),
        write_disposition="append"
    )
    print(load_info)
except Exception as e:
    print(f"Error during pipeline run: {e}")

print("step 2 completed")