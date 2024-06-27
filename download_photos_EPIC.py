import requests
import datetime
import argparse
import os
from dotenv import load_dotenv
from create_folder_images import download_picture


def get_path_photo():
    parser = argparse.ArgumentParser(
        description="Скачивает выбранное кол-во фотографий."
    )
    parser.add_argument(
        "count",
        nargs="?",
        help="Введите количество фотографий, которое\
                        нужно скачать",
        default=5
    )
    args = parser.parse_args()
    return args.count


def download_photos_nasa_epic(token, number_photos=5):
    photos_key = []
    photos_date = []
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    )
    response.raise_for_status()
    response = response.json()
    for url in response:
        photos_key.append(url["image"])
        photos_date.append(url["date"])

    for date_photo, number_photo in enumerate(photos_date):
        photos_date[date_photo] = datetime.datetime.strptime(number_photo, "%Y-%m-%d %H:%M:%S").strftime(
            "%Y/%m/%d"
        )

    for number_photo in range(0, number_photos):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photos_date[number_photo]}/png/{photos_key[number_photo]}.png"
        download_picture(url, picture_path=f"nasa_epic{number_photo + 1}.jpg", api_key=token)


if __name__ == "__main__":
    count = int(get_path_photo())
    load_dotenv()
    nasa_token = os.environ["NASA_API_KEY"]
    download_photos_nasa_epic(nasa_token, number_photos=count)
