from telegram_bot import TelegramBot
import os
from dotenv import load_dotenv, find_dotenv
if __name__ == '__main__':
    load_dotenv("token.env")

    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    TELEGRAM_API_TOKEN = os.environ["TELEGRAM_API_TOKEN"]
    bot = TelegramBot(OPENAI_API_KEY, TELEGRAM_API_TOKEN)
    bot.run()
