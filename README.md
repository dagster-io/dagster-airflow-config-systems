# dagster-airflow-config-systems

## to run as airflow

```bash

docker-compose build

docker-compose up

```

## to run as dagster

```bash

pip install -e ".[dev]"

dagster dev

```

## Slack API tokens

You will need to provide a slack token to both airflow and dagster to execute successfully for airflow you can create a default slack api connection and for dagster you can set the `SLACK_API_TOKEN` environment variable
