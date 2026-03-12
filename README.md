# Comprehensive Overview of the Project

This project encompasses an end-to-end data pipeline utilizing various tools and technologies such as Docker, Terraform, Airflow, Python, DLT, and Google Cloud Platform (GCP). The aim is to provide a robust and scalable architecture that efficiently manages data through its lifecycle.

## Architecture Diagram

![Architecture Diagram]()


## Getting Started

To set up your environment and get started with this project, follow the steps below:

### Prerequisites
- **Docker**: Ensure you have Docker installed for containerization.
- **Terraform**: Install Terraform for infrastructure provisioning.
- **Apache Airflow**: Set up Airflow for orchestrating the data pipeline.
- **Python**: Ensure you have Python installed for scripting and data manipulation.
- **Google Cloud SDK**: Install the Google Cloud SDK for GCP interactions.

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/opadotun-taiwo/data_eng_end_to_end_GCP.git
   cd data_eng_end_to_end_GCP
   ```

2. **Set Up Docker Environment**:
   - Build the Docker images defined in the `Dockerfile`.
   - Run the containers as defined in the `docker-compose.yml` file.
   
3. **Provision Infrastructure with Terraform**:
   - Navigate to the Terraform configurations.
   - Run the following commands to set up your GCP environment:
   ```bash
   terraform init
   terraform apply
   ```

4. **Setup Apache Airflow**:
   - Start Airflow web server and scheduler.
   - Configure your DAGs and tasks within Airflow to manage the pipeline.
   
5. **Data Pipeline Execution**:
   - The pipeline consists of several components: data loading, transformation, staging, intermediate processing, mart reporting, and machine learning features.
   - Initiate the pipeline through Airflow to automate workflows.

### Components Breakdown
- **Data Loading**: Loads raw data from various sources into GCP.
- **Transformation**: Processes and cleans the data using Python scripts.
- **Staging**: Stores processed data for further analysis.
- **Intermediate Processing**: Handles data transformations to create actionable data.
- **Mart Reporting**: Allows for reporting needs and visualizations.
- **ML Features**: Integrates machine learning models for predictions and insights.

### Conclusion
This overview provides a foundational understanding of the project. Check the documentation within each directory for more detailed instructions on specific components and functionalities.
