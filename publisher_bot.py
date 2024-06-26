import telegram
import os
from dotenv import load_dotenv

load_dotenv()
telegram_bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

bot = telegram.Bot(token=telegram_bot_token)
bot.send_message(chat_id=telegram_chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
