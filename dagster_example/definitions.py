import os
from .slack_resource import SlackResource

from dagster import Definitions, job, op


@op
def send_slack_message(slack: SlackResource):
    slack.send_file(
        channels="#random",
        content="hello world",
    )

@job
def slack_job():
    send_slack_message()


definitions = Definitions(
    jobs=[slack_job],
    resources={
        "slack": SlackResource(
            token=os.getenv("SLACK_API_TOKEN", "fake_token"),
            base_url=None,
            timeout=None,
            proxy=None,
        ),
    },
)
