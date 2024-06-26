import requests
import datetime
import argparse
import os
from dotenv import load_dotenv
from create_folder import download_picture
from create_folder import cerate_folder_for_images


def create_parser():
    parser = argparse.ArgumentParser(
        description="Скачивает выбранное кол-во фотографий."
    )
    parser.add_argument(
        "img",
        nargs="?",
        help="Введите количество фотографий, которое\
                        нужно скачать",
        default=None
    )
    args = parser.parse_args()
    return args.img


def download_photos_nasa_epic(token, count=5):
    if count == None:
        count = 5
    else:
        count = int(count)

    photos_key = []
    photos_date = []
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    )
    response.raise_for_status()
    response = response.json()
    for i in response:
        photos_key.append(i["image"])
        photos_date.append(i["date"])

    for i, w in enumerate(photos_date):
        photos_date[i] = datetime.datetime.strptime(w, "%Y-%m-%d %H:%M:%S").strftime(
            "%Y/%m/%d"
        )

    for i in range(0, count):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photos_date[i]}/png/{photos_key[i]}.png"
        download_picture(url, picture_path=f"nasa_epic{i + 1}.jpg", api_key=token)


if __name__ == "__main__":
    cerate_folder_for_images()
    count = create_parser()
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    download_photos_nasa_epic(nasa_token, count=count)
