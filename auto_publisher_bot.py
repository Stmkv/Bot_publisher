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
        nargs="?")
    args = parser.parse_args()
    return args.count


def auto_public_photo(bot, chat_id, img_list, count=1) -> None:
    for number_photo in range(count):
        if not img_list:
            img_list.extend(os.listdir("images/"))
            random.shuffle(img_list)

        photo_path = f"images/{img_list.pop()}"
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_id, photo=photo)


if __name__ == "__main__":
    count_photo_for_publication = int(get_number_photos())
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    publication_frequency = os.environ["PUBLICATION_FREQUENCY"]

    bot = telegram.Bot(token=telegram_bot_token)
    images = os.listdir("images/")
    random.shuffle(images)

    while True:
        auto_public_photo(bot, telegram_chat_id, images, count=count_photo_for_publication)
        time.sleep(float(publication_frequency))
