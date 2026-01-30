import time
from data_fetcher import connect_truedata
from algo_engine import generate_signal
from telegram_alert import send_alert

td = connect_truedata()

print("Algo started")

while True:
    price = 73500
    vwap = 73450
    volume = 2.0
    oi_change = 400

    signal = generate_signal(price, vwap, volume, oi_change)

    if signal:
        send_alert(f"SIGNAL: {signal}")

    time.sleep(60)
