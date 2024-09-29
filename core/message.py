import requests


def send_telegram_message(message):
    bot_token = "7220121804:AAHCmcpPlmNffi4aiSg-NR0fuWAnuphJDDY"
    chat_id = "6933049769"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    
    requests.post(url, json=payload)