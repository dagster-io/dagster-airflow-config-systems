from airflow.models.dag import DAG
from airflow.providers.slack.operators.slack import SlackAPIFileOperator
import pendulum

with DAG(
    dag_id="slack_example",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    default_args={
        "slack_conn_id": "slack",
    },
    max_active_runs=1,
) as dag:
    slack_operator_ = SlackAPIFileOperator(
        task_id="slack_operator_example",
        channel="#random",
        content="hello world",
    )
