import requests
import os
import urllib
import argparse
from upload_picture import download_picture
from dotenv import load_dotenv


def get_number_photos():
    parser = argparse.ArgumentParser(
        description='Скачивает заданное кол-во фотографий дня'
    )
    parser.add_argument('count',
                        help='Введите количество фотографий, которые\
                        нужно скачать',
                        default=5,
                        type=int,
                        nargs="?")
    args = parser.parse_args()
    return args.count


def get_photos_from_apod(token, count=5):
    photos = []
    params = {
        "count": count,
        "api_key": token,
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    response = response.json()
    for url in response:
        url_photo = url["url"]
        if get_file_extension(url_photo) == ".jpg":
            photos.append(url_photo)
    for number, url in enumerate(photos, start=1):
        download_picture(url, picture_path=f"nasa_apod{number}.jpg")


def get_file_extension(url: str) -> str:
    parse = urllib.parse.urlsplit(url)
    patch = parse[2]
    extension = os.path.splitext(patch)[1]
    return extension


if __name__ == "__main__":
    quantity = get_number_photos()
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    get_photos_from_apod(nasa_token, count=quantity)
