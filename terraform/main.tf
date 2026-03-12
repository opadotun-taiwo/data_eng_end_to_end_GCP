terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.21.0"
    }
  }
}

provider "google" {
  # If a JSON key file path is set, read its contents. Otherwise rely on
  # Application Default Credentials (ADC) or environment variable.
  project = var.project
  region  = var.region
}

resource "google_storage_bucket" "trips_bucket" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}


resource "google_bigquery_dataset" "trips_dataset" {
  dataset_id                 = var.dataset_id
  location                   = var.region
  delete_contents_on_destroy = true
}
