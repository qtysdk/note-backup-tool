import typing as t

import click


class MissingAPITokenError(click.ClickException):
    """Exception raised when the API token is missing."""

    def __init__(self, message=None):
        super().__init__(message)

    def show(self) -> None:
        click.echo("env[NBC_HACKMD_API_TOKEN] is not set", err=True)


def load_api_token():
    import os
    token = os.environ.get('NBC_HACKMD_API_TOKEN')
    if not token:
        raise MissingAPITokenError()
    return token
