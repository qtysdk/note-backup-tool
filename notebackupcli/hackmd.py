import json

import click
import requests


class RequestError(click.ClickException):
    """Exception raised when the API token is missing."""

    def __init__(self, code, message=None):
        self.code = code
        super().__init__(message)

    def show(self) -> None:
        click.echo(f"request error. http_status={self.code}, response={self.message}", err=True)


def pretty(data):
    """
    Print JSON data in a pretty formatted way.

    :param data: The JSON data to print. Can be a dictionary or a JSON string.
    """
    if isinstance(data, str):
        # If the data is a string, try to load it as JSON
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            print("Invalid JSON string.")
            return

    pretty_json = json.dumps(data, indent=4, sort_keys=True)
    return pretty_json


def _hackmd_request(api_token, url):
    """
    Make a request to a specified HackMD API endpoint.

    :param api_token: API token for authentication
    :param url: URL of the HackMD API endpoint
    :return: Response data as a pretty-formatted string, or raises RequestError if request failed
    """
    headers = {'Authorization': f'Bearer {api_token}'}

    response = requests.get(url, headers=headers)

    if response.ok:
        return pretty(response.text)
    else:
        raise RequestError(response.status_code, response.text)


def fetch_user_data(api_token):
    """
    Fetch user data from HackMD API.

    :param api_token: API token for authentication
    :return: Response data as a string or None if request failed
    """
    return _hackmd_request(api_token, 'https://api.hackmd.io/v1/me')


def list_notes(api_token):
    """
    List notes from the HackMD API.

    :param api_token: API token for authentication
    :return: Response data as a string or None if request failed
    """
    # Replace the URL with the correct endpoint for listing notes
    notes_url = 'https://api.hackmd.io/v1/notes'
    return _hackmd_request(api_token, notes_url)


def get_note(api_token, note_id):
    """
    Get a specific note from the HackMD API.

    :param api_token: API token for authentication
    :param note_id: The ID of the note to fetch
    :return: Response data as a string or None if request failed
    """
    # Construct the URL with the note_id
    note_url = f'https://api.hackmd.io/v1/notes/{note_id}'
    return _hackmd_request(api_token, note_url)
