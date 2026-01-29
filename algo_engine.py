# algo_engine.py
import numpy as np

# ATM strike calculation
def get_atm_strike(spot, gap=50):
    return round(spot / gap) * gap

# Trend detection
def get_trend(spot, vwap, ema20, ema50):
    if spot > vwap and ema20 > ema50:
        return "UP"
    elif spot < vwap and ema20 < ema50:
        return "DOWN"
    else:
        return "CHOP"

# Big player detection
def is_big_player(price_change, oi_change, volume, avg_volume):
    return price_change > 0 and oi_change > 0 and volume > avg_volume

# Fake move detection
def is_fake(price_change, oi_change, spread, time, no_trade_times):
    if oi_change <= 0:
        return True
    if spread > 10:
        return True
    if time in no_trade_times:
        return True
    return False
