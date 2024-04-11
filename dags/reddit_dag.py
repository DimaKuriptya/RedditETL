from airflow import DAG
from datetime import datetime
import pathlib
import sys
import os
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline


default_args = {
    'owner': 'DimaKuriptya',
    'start_date': datetime(2024, 4, 8)
}

file_postfix = datetime.now().strftime('%Y%m%d')

with DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
) as dag:
    # Extraction from reddit
    extract = PythonOperator(
        task_id='reddit_extraction',
        python_callable=reddit_pipeline,
        op_kwargs={
            'file_name': f'reddit{file_postfix}',
            'subreddit': 'dataengineering',
            'time_filter': 'day',
            'limit': 100
        }
    )

    # Uploading to S3
    upload_s3 = PythonOperator(
        task_id='s3_upload',
        python_callable=upload_s3_pipeline,
    )

    extract >> upload_s3
