import requests
import os
import urllib
import shutil


def get_photos_from_apod(count: int) -> str:
    photos = []
    params = {
        "count": count,
        "api_key": "uBdF2I4UKAoqADW607qz73gjPAerS8a8f9dyjVuR",
    }
    response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
    response.raise_for_status()
    response = response.json()
    for i in response:
        url_photo = i["url"]
        if get_file_extension(url_photo) == ".jpg":
            photos.append(url_photo)
    for number, url in enumerate(photos):
        download_picture(url, f"nasa_apod{number}.jpg")


def get_file_extension(url: str) -> str:
    parse = urllib.parse.urlsplit(url) # распарсивает по элементам
    return os.path.splitext(parse[2])[1] # разделяет на формат, выбирает его b возвращает


def download_picture(
    url: str,
    picture_path: str,
) -> None:
    response = requests.get(url)
    response.raise_for_status()

    with open(picture_path, "wb") as file:
        file.write(response.content)
    shutil.move(picture_path, "images")  # Перемещение фотографии в папку images

if __name__ == "__main__":
    get_photos_from_nasa(5)
