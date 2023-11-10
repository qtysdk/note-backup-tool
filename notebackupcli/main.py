import json
from datetime import datetime

import click
from rich.console import Console
from rich.table import Table

from notebackupcli.hackmd import fetch_user_data, get_note, list_notes
from notebackupcli.markdown import convert
from notebackupcli.utils import load_api_token


class CLIContext:
    def __init__(self, json_output=False):
        self._api_token = load_api_token()
        self._json_output = json_output

    @property
    def api_token(self):
        return self._api_token

    @property
    def json_output(self):
        return self._json_output


@click.group(name="note-backup-tool")
@click.option('--json', is_flag=True, help="Output in JSON format")
@click.pass_context
def main(ctx: click.Context, json):
    if ctx.obj is None:
        ctx.obj = CLIContext(json_output=json)


@main.command()
@click.pass_context
def me(ctx: click.Context):
    """
    Display information about the current user.

    This command fetches and displays details of the current user's profile. This might include username, email, and other relevant settings or status information.

    Args:
        ctx: The Click context which may contain user-specific data or configurations.
    """

    data = fetch_user_data(ctx.obj.api_token)
    if ctx.obj.json_output:
        print(data)

    def show_table(data):
        table = Table(title="User Information")

        # 添加列
        table.add_column("ID", justify="left")
        table.add_column("Name", justify="left")
        table.add_column("Email", justify="left")

        # 添加行
        table.add_row(data["id"], data["name"], data["email"])

        # 显示表格
        console = Console()
        console.print(table)

    show_table(json.loads(data))


@main.command()
@click.pass_context
def list(ctx):
    """
    List notes with an option to display in table format.
    """

    data = list_notes(ctx.obj.api_token)
    if ctx.obj.json_output:
        print(data)
        return

    def show_table(data):
        """
        Display the given data as a table.

        :param data: JSON array of note data
        """
        notes = json.loads(data)
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim")
        table.add_column("Title")
        table.add_column("Published At", justify="right")

        for note in notes:
            published_at = note['publishedAt']
            if published_at:
                iso_datetime = datetime.fromtimestamp(published_at / 1000).isoformat()
            else:
                iso_datetime = 'not published'
            table.add_row(note['id'], note['title'], iso_datetime)

        console = Console()
        console.print(table)

    show_table(data)


@main.command()
@click.argument('note_id')
@click.pass_context
def get(ctx: click.Context, note_id):
    """
    Retrieve and convert a specific note.

    This command fetches a note identified by its ID and converts it into a specified format. The converted note is then saved as a markdown file named '{note_id}.md'.

    Args:
        ctx: The Click context holding shared data like the API token.
        note_id: The unique identifier of the note to be fetched and converted.
    """

    # Retrieve note data
    note_data = json.loads(get_note(ctx.obj.api_token, note_id))
    content = note_data.get('content')

    # Convert the content (assuming your 'convert' function does this)
    output = convert(content)

    # Save the output to a file named '{note_id}.md'
    file_name = f"{note_id}.md"
    with open(file_name, 'w') as file:
        file.write(output)

    # Optional: Print a message to indicate successful saving
    print(f"Note saved as {file_name}")
