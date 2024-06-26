import telegram
import os
import random
import time
import argparse
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description="Публикует заданное кол-во фотографий за раз."
    )
    parser.add_argument(
        "count",
        help="Введите количество фотографий, которые\
                        нужно опубликовать",
    )
    args = parser.parse_args()
    return args.count


def auto_public_photo(bot, chat_id, img_list, count=1) -> None:
    for i in range(count):
        if not img_list:
            img_list.extend(os.listdir("images/"))
            random.shuffle(img_list)

        photo_path = f"images/{img_list.pop()}"
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_id, photo=photo)


if __name__ == "__main__":
    count_photo_for_publication = int(create_parser())
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    publication_frequency = os.environ["PUBLICATION_FREQUENCY"]

    bot = telegram.Bot(token=telegram_bot_token)
    img_list = os.listdir("images/")
    random.shuffle(img_list)

    while True:
        auto_public_photo(bot, telegram_chat_id, img_list, count=count_photo_for_publication)
        time.sleep(float(publication_frequency))
