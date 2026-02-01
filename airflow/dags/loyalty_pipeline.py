from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(
dag_id='cpg_loyalty_demo',
start_date=datetime(2025, 1, 1),
schedule='@daily',
catchup=False,
tags=['loyalty', 'cpg', 'demo'],
) as dag:
dbt_run = BashOperator(
task_id='dbt_run_transformations',
bash_command='cd /opt/airflow/dbt && dbt run --profiles-dir /opt/airflow/dbt',
)
dbt_test = BashOperator(
task_id='dbt_test',
bash_command='cd /opt/airflow/dbt && dbt test',
)
dummy_recommender = BashOperator(
task_id='run_recommender',
bash_command='python /opt/airflow/recommender/src/dummy_recommender.py',
)
dbt_run >> dbt_test >> dummy_recommender
