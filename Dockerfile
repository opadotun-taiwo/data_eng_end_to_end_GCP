FROM apache/airflow:2.8.4-python3.11

USER root
RUN apt-get update && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir \
    dlt==1.22.2 \
    dbt-core \
    dbt-bigquery \
    google-cloud-bigquery \
    google-cloud-storage \
    gcsfs \
    pandas \
    pyarrow \
    requests