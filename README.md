# Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Overview

The pipeline is designed to:

1. Extract data from Reddit using its API.
2. Store the raw data into an S3 bucket from Airflow.
3. Transform the data using AWS Glue and Amazon Athena.
4. Load the transformed data into Amazon Redshift for analytics and querying.

## Architecture
1. **Reddit API**: Source of the data.
2. **Apache Airflow & Celery**: Orchestrates the ETL process and manages task distribution.
3. **PostgreSQL**: Temporary storage and metadata management.
4. **Amazon S3**: Raw data storage.
5. **AWS Glue**: Data cataloging and ETL jobs.
6. **Amazon Athena**: SQL-based data transformation.
7. **Amazon Redshift**: Data warehousing and analytics.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation
- Python 3.11 or higher

## System Setup
1. Clone the repository.
   ```bash
    git clone https://github.com/DimaKuriptya/RedditETL.git
   ```
2. Create a virtual environment.
   ```bash
    python3 -m venv venv
   ```
3. Activate the virtual environment.
   ```bash
    source venv/bin/activate
   ```
4. Install the dependencies.
   ```bash
    pip install -r requirements.txt
   ```
5. Create a folder `config` in the root directory and a file `config.conf` inside it. Fill the file by the folowing template:
```bash
[database]
database_host = localhost
database_name = airflow_reddit
database_port = 5432
database_username = postgres
database_password = postrgres

[file_paths]
input_path = /opt/airflow/data/input
output_path = /opt/airflow/data/output

[api_keys]
reddit_secret_key = [SECRET KEY HERE]
reddit_client_id = [CLIENT ID HERE]

[aws]
aws_access_key_id = [aws access key id]
aws_secret_access_key = [aws secret key]
aws_session_token = [aws session token]
aws_region = [aws region]
aws_bucket_name = [s3 bucket name]

[etl_settings]
batch_size = 100
error_handling = abort
log_level = info
```

6. Starting the containers
   
   Run airflow-init:
   ```bash
    docker-compose up airflow-init -d
   ```
   Wait for airflow-init container to end its job and then run the following command:
   ```
   docker-compose up -d
   ```
8. Launch the Airflow web UI.
   ```bash
    open http://localhost:8080
   ```
