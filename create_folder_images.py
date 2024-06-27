import os
import requests
import shutil


def download_picture(
    url: str,
    picture_path: str,
    api_key=''
) -> None:
    os.makedirs("images", exist_ok=True)
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(picture_path, "wb") as file:
        file.write(response.content)
    shutil.move(picture_path, "images")
