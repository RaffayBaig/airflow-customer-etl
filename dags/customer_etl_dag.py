from datetime import timedelta
import sys

import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# Tell Python where our ETL scripts are
sys.path.insert(0, "/opt/airflow/scripts")

from extract import extract
from transform import transform
from load import load


with DAG(
    dag_id="customer_etl_pipeline",
    description="Customer CSV ETL pipeline",
    start_date=pendulum.datetime(2026, 9, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=1),
    },
    tags=["etl", "customers", "postgres"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task