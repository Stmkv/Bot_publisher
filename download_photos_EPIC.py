import requests
import datetime
import argparse
from create_folder import download_picture


def create_parser():
    parser = argparse.ArgumentParser(
        description="Скачивает заданное кол-во фотографий."
    )
    parser.add_argument(
        "count",
        help="Введите количество фотографий, которые\
                        нужно скачать",
    )
    args = parser.parse_args()
    return args.count


def download_photos_nasa_epic(count=5):
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
        download_picture(url, picture_path=f"nasa_epic{i+1}.jpg", api_key = "uBdF2I4UKAoqADW607qz73gjPAerS8a8f9dyjVuR")




if __name__ == "__main__":
    count = int(create_parser())
    download_photos_nasa_epic(count=count)
