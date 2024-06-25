import requests
import os
import urllib
import shutil
import datetime


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
        photos_date[i] = datetime.datetime.strptime(w, "%Y-%m-%d %H:%M:%S").strftime("%Y/%m/%d"
        )

    for i in range(0, count):
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photos_date[i]}/png/{photos_key[i]}.png"
        download_picture(url, f"nasa_epic{i+1}.jpg")


def download_picture(
    url: str,
    picture_path: str,
) -> None:
    params = {"api_key": "uBdF2I4UKAoqADW607qz73gjPAerS8a8f9dyjVuR"}
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(picture_path, "wb") as file:
        file.write(response.content)
    shutil.move(picture_path, "images")  # Перемещение фотографии в папку images


download_photos_nasa_epic(count=5)
