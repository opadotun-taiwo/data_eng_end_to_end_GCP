variable "credentials_path" {
  description = "Path to GCP service account JSON key file. Leave empty to use Application Default Credentials (ADC)."
  type        = string
  default     = ""
  sensitive   = true
}

variable "project" {
  description = "GCP project ID"
  type        = string
  default     = "gothic-sled-453213-i2"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Name of the Google Cloud Storage bucket (must be globally unique)."
  type        = string
  default     = "gothic-sled-453213-i2-trips-bucket"
}

variable "dataset_id" {
  description = "data set id in big query"
  type        = string
  default     = "trips_dataset"
}
