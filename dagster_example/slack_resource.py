from dagster import ConfigurableResource
from slack_sdk import WebClient
from slack_sdk.web.slack_response import SlackResponse
from pydantic import Field
from functools import cached_property
from pathlib import Path
from typing import Sequence


class SlackResource(ConfigurableResource):
    token: str = Field(
        description="Slack API Token.",
    )
    base_url: str | None = Field(
        description="A string representing the Slack API base URL. If not set than default WebClient BASE_URL will use (``https://www.slack.com/api/``).",
    )
    timeout: int | None = Field(
        description="The maximum number of seconds the client will wait to connect and receive a response from Slack. If not set than default WebClient value will use.",
    )
    proxy: str | None = Field(
        description="Proxy to make the Slack API call.",
    )

    @cached_property
    def client(self) -> WebClient:
        """Get the underlying slack_sdk.WebClient (cached)."""
        client_kwargs = {
            "token": self.token,
            "proxy": self.proxy,
        }
        if self.base_url is not None:
            client_kwargs["base_url"] = self.base_url
        if self.timeout is not None:
            client_kwargs["timeout"] = self.timeout
        return WebClient(**client_kwargs)

    def call(self, api_method: str, **kwargs) -> SlackResponse:
        return self.client.api_call(api_method, **kwargs)

    def send_file(
        self,
        *,
        channels: str | Sequence[str] | None = None,
        file: str | Path | None = None,
        content: str | None = None,
        filename: str | None = None,
        filetype: str | None = None,
        initial_comment: str | None = None,
        title: str | None = None,
    ) -> SlackResponse:
        if not ((not file) ^ (not content)):
            raise ValueError("Either `file` or `content` must be provided, not both.")
        elif file:
            file = Path(file)
            with open(file, "rb") as fp:
                if not filename:
                    filename = file.name
                return self.client.files_upload(
                    file=fp,
                    filename=filename,
                    filetype=filetype,
                    initial_comment=initial_comment,
                    title=title,
                    channels=channels,
                )

        return self.client.files_upload(
            content=content,
            filename=filename,
            filetype=filetype,
            initial_comment=initial_comment,
            title=title,
            channels=channels,
        )
