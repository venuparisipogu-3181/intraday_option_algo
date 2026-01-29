# alert_runner.py
import time
from data_fetcher import live_data
from algo_engine import get_atm_strike, get_trend, is_big_player, is_fake
from telegram_alert import send_telegram_alert
import pandas as pd

BOT_TOKEN = "<YOUR_BOT_TOKEN>"
CHAT_ID = "<YOUR_CHAT_ID>"

INDEX_GAPS = {
    "NIFTY-I": 50,
    "BANKNIFTY-I": 100,
    "SENSEX-I": 50
}

NO_TRADE_TIMES = ["12:00:00", "12:30:00"]

while True:
    for symbol, data in live_data.items():
        if not data:
            continue  # skip if no tick yet

        spot = data['ltp']
        gap = INDEX_GAPS[symbol]
        atm = get_atm_strike(spot, gap)

        # For example: simple trend using last few ltp (replace with real EMA/VWAP)
        ltp_list = [spot]  # ideally store last N ticks for EMA/VWAP
        vwap = np.mean(ltp_list)
        ema20 = np.mean(ltp_list)
        ema50 = np.mean(ltp_list)
        trend = get_trend(spot, vwap, ema20, ema50)

        price_change = 1  # placeholder, replace with actual delta
        oi_change = data['oi']
        spread = data['best_ask'] - data['best_bid']

        if not is_fake(price_change, oi_change, spread, data['time'], NO_TRADE_TIMES) and is_big_player(price_change, oi_change, spread, spread):
            message = f"{symbol} Signal: {trend}\nSpot: {spot}\nATM Strike: {atm}"
            send_telegram_alert(BOT_TOKEN, CHAT_ID, message)

    time.sleep(60)
