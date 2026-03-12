# Terraform credentials and usage

Best practices for GCP credentials with Terraform:

- Prefer using Application Default Credentials (ADC) or setting the environment variable:

  - Linux/macOS:

    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
    ```

  - Windows PowerShell:

    ```powershell
    $env:GOOGLE_APPLICATION_CREDENTIALS = 'C:\path\to\key.json'
    ```

- Do NOT commit JSON key files into the repository. They are ignored by `.gitignore`.
- In CI, store the key as a secret and set `GOOGLE_APPLICATION_CREDENTIALS` during the job.
- Alternatively, rely on Workload Identity / instance service accounts when running in GCP.

If you must provide a path to a JSON key file to Terraform, use the `credentials_path` variable
and pass it via a secure `*.tfvars` file or CI variable (do not check in the tfvars file).

## Example `terraform.tfvars` (do not commit)

```hcl
credentials_path = "/path/to/key.json"
project          = "gothic-sled-453213-i2"
region           = "us-central1"
# bucket_name must be set to a globally unique value:
# bucket_name     = "my-unique-bucket-name-12345"
```

When you run Terraform, specify the file explicitly or use the default:

```bash
terraform init
terraform apply -var-file="terraform.tfvars"
```

The configuration also creates a Google Cloud Storage bucket. You must supply
`bucket_name` either via a tfvars file or on the command line (it has no
sensible default and must be globally unique).

After apply you can reference the bucket via the `bucket_self_link` output.
