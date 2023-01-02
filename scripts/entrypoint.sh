#!/usr/bin/env bash
airflow db init
pip install -r /opt/airflow/requirements.txt
airflow users create --username airflow --firstname Madhav --lastname Dube --password airflow --role Admin --email madhav.dubey9@gmail.com
airflow connections add postgres_conn --conn-uri 'postgres://user:password@db:5432/my_db'
airflow webserver