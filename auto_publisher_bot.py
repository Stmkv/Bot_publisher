import telegram
import os
import random
import time
import argparse
from dotenv import load_dotenv


def get_number_photos():
    parser = argparse.ArgumentParser(
        description="Публикует заданное кол-во фотографий за раз."
    )
    parser.add_argument(
        "count",
        help="Введите количество фотографий, которые\
                        нужно опубликовать",
        default=1,
        type=int,
        nargs="?")
    args = parser.parse_args()
    return args.count


def auto_public_photo(bot, chat_ids, img, count=1) -> None:
    for number_photo in range(count):
        if not img:
            img.extend(os.listdir("images/"))
            random.shuffle(img)

        photo_path = f"images/{img.pop()}"
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_ids, photo=photo)


if __name__ == "__main__":
    photo_for_publication = get_number_photos()
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    publication_frequency = os.environ["PUBLICATION_FREQUENCY"]

    bot = telegram.Bot(token=telegram_bot_token)
    images = os.listdir("images/")
    random.shuffle(images)

    while True:
        auto_public_photo(bot, telegram_chat_id, images, count=photo_for_publication)
        time.sleep(float(publication_frequency))
