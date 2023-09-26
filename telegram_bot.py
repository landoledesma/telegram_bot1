import openai
import requests
import time

class TelegramBot:
    def __init__(self, openai_key, telegram_token):
        openai.api_key = openai_key
        self.TOKEN = telegram_token

    def get_updates(self, offset):
        url = f"https://api.telegram.org/bot{self.TOKEN}/getUpdates"
        params = {"timeout": 100, "offset": offset}
        response = requests.get(url, params=params)
        return response.json()["result"]

    def send_messages(self, chat_id, text):
        url = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage"
        params = {"chat_id": chat_id, "text": text}
        response = requests.post(url, params=params)
        return response

    def get_openai_response(self, prompt):
        model_engine = "text-davinci-003"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=80,
            n=1,
            stop=" END",
            temperature=0.3
        )
        return response.choices[0].text.strip()

    def run(self):
        print("Starting bot...")
        offset = 0
        while True:
            updates = self.get_updates(offset)
            if updates:
                for update in updates:
                    offset = update["update_id"] + 1
                    chat_id = update["message"]["chat"]['id']
                    if 'text' in update["message"]:
                        user_message = update["message"]["text"]
                        print(f"Received message: {user_message}")
                        GPT_response = self.get_openai_response(user_message)
                        resp = self.send_messages(chat_id, GPT_response)
                        print(f"send message:{resp}")
            else:
                time.sleep(1)
