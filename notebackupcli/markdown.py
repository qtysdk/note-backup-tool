import os
from typing import Any, Dict
from urllib.parse import urlparse

import mistune
import requests
from mistune import BlockState
from mistune.renderers.markdown import MarkdownRenderer


def save_to_local(url):
    # Parse the URL to extract the filename
    parsed_url = urlparse(url)
    file_name = os.path.basename(parsed_url.path)

    # Create 'images' directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    local_file_path = os.path.join('images', file_name)

    # Check if the file already exists locally
    if not os.path.exists(local_file_path):
        # Attempt to download the file
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(local_file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print(f"Unable to download the file: {url}")
        except Exception as e:
            print(f"Error occurred during download: {e}")

    return local_file_path


class ImageLinkRenderer(MarkdownRenderer):
    def __init__(self):
        super().__init__()
        self.image_links = []

    def image(self, token: Dict[str, Any], state: BlockState) -> str:
        token['attrs']['url'] = save_to_local(token['attrs']['url'])
        result = super().image(token, state)
        return result


def convert(markdown_text: str):
    markdown = mistune.create_markdown(renderer=ImageLinkRenderer())
    return markdown(markdown_text)
