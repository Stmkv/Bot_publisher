import telegram
import os
import random

from dotenv import load_dotenv


def public_photo(chat_id):
    img_list = os.listdir(r"images/")
    photo_path = f"images/{random.choice(img_list)}"
    bot.send_photo(chat_id, photo=open(photo_path, 'rb'))


if __name__ == "__main__":
    load_dotenv()
    telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=telegram_bot_token)
    public_photo(telegram_chat_id)
