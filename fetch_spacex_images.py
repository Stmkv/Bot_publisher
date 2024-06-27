import argparse
import requests
from create_folder_images import download_picture


def get_number_photos():
    parser = argparse.ArgumentParser(
        description="Скачивает выбранное кол-во фотографий."
    )
    parser.add_argument(
        "id",
        nargs="?",
        help="Введите id запуска",
        default="latest"
    )
    args = parser.parse_args()
    return args.id


def fetch_spacex_last_launch(launch_id="latest") -> None:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    response = response.json()
    for number, pictures in enumerate(response["links"]["flickr"]["original"], start=1):
        download_picture(pictures, f"spacex{number}.jpg")


if __name__ == "__main__":
    id = get_number_photos()
    print(id)
    fetch_spacex_last_launch(launch_id=id)
