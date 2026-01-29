# telegram_alert.py
import requests

def send_telegram_alert(8289933882:AAGgTyAhFHYzlKbZ_0rvH8GztqXeTB6P-yQ, 2115666034, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=payload)
        return True
    except Exception as e:
        print("Telegram Error:", e)
        return False
