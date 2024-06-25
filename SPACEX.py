import requests
import os
import shutil
import urllib


def cerate_folder_for_images() -> None:
    if not os.path.exists("images"):
        os.makedirs("images")


def download_picture(
    url: str,
    picture_path: str,
) -> None:
    response = requests.get(url)
    response.raise_for_status()

    with open(picture_path, "wb") as file:
        file.write(response.content)
    shutil.move(picture_path, "images")  # Перемещение фотографии в папку images


def fetch_spacex_last_launch() -> None:
    response = requests.get("https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a")
    response.raise_for_status()

    response = response.json()
    for number, pictures in enumerate(response["links"]["flickr"]["original"]):
        download_picture(pictures, f"spacex{number+1}.jpg")


if __name__ == "__main__":
    cerate_folder_for_images()
    fetch_spacex_last_launch()
