from setuptools import find_packages, setup

setup(
    name="airflow-airflow-config-systems",
    packages=find_packages(),
    install_requires=[
        "dagster>=1.3.0",
        "slack_sdk>=3.21.3"
    ],
    extras_require={"dev": ["dagit"]},
)
