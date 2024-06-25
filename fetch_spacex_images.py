import argparse
import requests
from create_folder import cerate_folder_for_images
from create_folder import download_picture


def create_parser():
    parser = argparse.ArgumentParser(
        description='Скачивает фотографии с запуска'
    )
    parser.add_argument('id', help='Введите id запуска')
    args = parser.parse_args()
    return args.id


def fetch_spacex_last_launch(launch_id="latest") -> None:
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    response = response.json()
    for number, pictures in enumerate(response["links"]["flickr"]["original"]):
        download_picture(pictures, f"spacex{number+1}.jpg")


if __name__ == "__main__":
    id = create_parser()
    cerate_folder_for_images()
    fetch_spacex_last_launch(launch_id=id)
