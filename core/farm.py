import requests
import time

from smart_airdrop_claimer import base
from core.headers import headers
from core.message import send_telegram_message


def start_farming(token, proxies=None):
    url = "https://game-domain.blum.codes/api/v1/farming/start"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def claim_farming(token, proxies=None):
    url = "https://game-domain.blum.codes/api/v1/farming/claim"

    try:
        response = requests.post(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def process_farming(token, proxies=None):
    process_claim = claim_farming(token=token, proxies=proxies)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    try:
        balance = float(process_claim["availableBalance"])
        base.log(
            f"{base.white}Auto Farm: {base.green}Claim Success | New balance: {balance:,} points"
        )
        message = f"Claimed Success! New Balance: {balance:,} (Timestamp: {timestamp} UTC)"
        send_telegram_message(message)

    except:
        message = process_claim["message"]
        base.log(f"{base.white}Auto Farm: {base.red}Claim Error | {message}")
        message = f"Claim Error! (Timestamp: {timestamp} UTC)"
        send_telegram_message(message)


    process_start = start_farming(token=token, proxies=proxies)
    farmed = float(process_start["balance"])
    if farmed > 0:
        base.log(
            f"{base.white}Auto Farm: {base.yellow}Farming | Farmed point: {farmed:,} points"
        )
        message = f"Farmed Tokens: {farmed:,} ! (Timestamp: {timestamp} UTC)"
        send_telegram_message(message)

    else:
        base.log(f"{base.white}Auto Farm: {base.green}Start Farming Success")
        message = f"Started Farming Successfully! (Timestamp: {timestamp} UTC)"
        send_telegram_message(message)

