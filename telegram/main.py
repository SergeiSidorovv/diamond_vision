import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()

    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    FILE_PATH = "text.txt"  

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    chat_id = input()
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    r = requests.post(url, json=payload)

    if r.status_code == 200:
        print("Отправлено.")
    else:
        print("Ошибка:", r.text)

if __name__ == '__main__':
    main()