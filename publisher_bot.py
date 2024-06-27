import telegram
import os
import random
import argparse
from dotenv import load_dotenv


def get_path_photo():
    parser = argparse.ArgumentParser(
        description="Публикует выбранную фотографию."
    )
    parser.add_argument(
        "img",
        nargs="?",
        help="Введите фотографию, которую\
                        нужно опубликовать",
        default=None
    )
    args = parser.parse_args()
    return args.img


def public_photo(chat_id, img_list, img = None):
    if img == None:
        photo_path = f"images/{random.choice(img_list)}"
        bot.send_photo(chat_id, photo=open(photo_path, 'rb'))
    else:
        photo_path = f"images/{img}"
        bot.send_photo(chat_id, photo=open(photo_path, 'rb'))


if __name__ == "__main__":
    load_dotenv()
    img = get_path_photo()
    imges = os.listdir(r"images/")
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=telegram_bot_token)
    public_photo(telegram_chat_id, imges, img)
