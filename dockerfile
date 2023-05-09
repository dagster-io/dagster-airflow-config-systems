FROM apache/airflow:2.5.2-python3.10
RUN pip install --no-cache-dir --user --upgrade pip
RUN pip install apache-airflow-providers-slack==7.2.0
USER 50000
