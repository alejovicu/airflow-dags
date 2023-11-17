import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

test_dag_alejandro = DAG(
     dag_id="test_dag_demo",
     start_date=datetime.datetime(2023, 11, 16),
     schedule="@daily",
)
EmptyOperator(task_id="task", dag=test_dag_alejandro)
