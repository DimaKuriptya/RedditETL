from airflow import DAG
from datetime import datetime
import pathlib
import sys
from airflow.operators.python import PythonOperator

sys.path.insert(0, pathlib.Path(__file__).parent.parent)
from pipelines.reddit_pipeline import reddit_pipeline



default_args = {
    'owner': 'DimaKuriptya',
    'start_date': datetime(2024, 4, 8)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)


# Extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

# Uploading to S3
