from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import dag, task
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


@dag(
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['stock_prices'],
)
def ingest_stock_data_etl():
    """
    ETL to ingest data into Postgres DB
    """
    @task()
    def extract_push():
        d = datetime.today()
        last_seven_days_date = datetime.strftime(d.date() - timedelta(days=7), '%Y-%m-%d')
        yesterday_date = datetime.strftime(d.date() - timedelta(days=1), '%Y-%m-%d')
        faang_list = ["AAPL","META", "AMZN", "NFLX", "GOOG"]
        df = pd.DataFrame()
        for comp in faang_list:
            data = yf.download(comp, start=last_seven_days_date, end=yesterday_date)
            data['company']=comp
            df = pd.concat([df, data])

        postgres_sql_upload = PostgresHook(postgres_conn_id='postgres_default')
        engine = postgres_sql_upload.get_sqlalchemy_engine()
        tmp_table = '"public.stock_data_tmp"'
        target_table = '"public.stock_data"'
        engine.execute(f'truncate table {tmp_table}')
        df = df.reset_index()
        df.to_sql('public.stock_data_tmp', postgres_sql_upload.get_sqlalchemy_engine(),
                  if_exists='append',
                  index=False, chunksize=100)
        engine.execute(f"""
            insert into {target_table}
            select * from {tmp_table}
            on conflict do nothing
        """)
        engine.execute(f'truncate table {tmp_table}')
        engine.execute(f"delete from {target_table} where the_timestamp < now() - interval '240 days' ")

    extract_push()


dag = ingest_stock_data_etl()
