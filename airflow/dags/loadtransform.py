from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


DBT_PROJECT_DIR = "C:/Users/admin/Desktop/complete_data_project/trips/dbt"
DBT_PROFILES_DIR = "C:/Users/admin/Desktop/complete_data_project/trips/dbt_profiles"

# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}


dag = DAG(
    dag_id="dlt_trip_pipeline",
    default_args=default_args,
    description="Run DLT pipeline script and transform",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False
)


run_dlt_pipeline = BashOperator(
    task_id="run_dlt_pipeline",
    bash_command="python C:/Users/admin/Desktop/complete_data_project/trips/load/pipeline.py",
    dag=dag
)

dbt_task = BashOperator(
    task_id="run_dbt_build",
    bash_command=f"""
        cd {DBT_PROJECT_DIR} && \
        dbt build --profiles-dir {DBT_PROFILES_DIR}
    """
)

run_dlt_pipeline >> dbt_task