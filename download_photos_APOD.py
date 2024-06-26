import requests
import os
import urllib
import argparse
from create_folder import download_picture
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description='Скачивает заданное кол-во фотографий дня'
    )
    parser.add_argument('count', help='Введите количество фотографий, которые\
                        нужно скачать')
    args = parser.parse_args()
    return args.count


def get_photos_from_apod(count: int, token: str) -> None:
    photos = []
    params = {
        "count": count,
        "api_key": token,
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    response = response.json()
    for i in response:
        url_photo = i["url"]
        if get_file_extension(url_photo) == ".jpg":
            photos.append(url_photo)
    for number, url in enumerate(photos):
        download_picture(url, picture_path=f"nasa_apod{number + 1}.jpg")


def get_file_extension(url: str) -> str:
    parse = urllib.parse.urlsplit(url)
    return os.path.splitext(parse[2])[
        1
    ]


if __name__ == "__main__":
    count = create_parser()
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    get_photos_from_apod(count, nasa_token)