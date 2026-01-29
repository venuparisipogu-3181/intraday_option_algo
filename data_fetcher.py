# data_fetcher.py
from truedata_ws.websocket.TD import TD

# --- TrueData credentials ---
USERNAME = "your_username"
PASSWORD = "your_password"
LIVE_PORT = 8082

# --- Initialize TrueData connection ---
td = TD(USERNAME, PASSWORD, live_port=LIVE_PORT)

# --- Subscribe symbols ---
SYMBOLS = ["NIFTY-I", "BANKNIFTY-I", "SENSEX-I"]

# --- Data storage dictionary ---
live_data = {
    "NIFTY-I": {},
    "BANKNIFTY-I": {},
    "SENSEX-I": {}
}

# --- Tick callback function ---
def on_tick(tick):
    symbol = tick['symbol']
    live_data[symbol] = {
        "ltp": tick['ltp'],
        "oi": tick['oi'],
        "best_bid": tick['best_bid_price'],
        "best_ask": tick['best_ask_price'],
        "time": tick['time']
    }

# --- Register callback ---
td.trade_callback(on_tick)

# --- Start streaming ---
td.start_live_data(SYMBOLS)

# --- Optional stop function ---
def stop_stream():
    td.stop_live_data(SYMBOLS)
    td.disconnect()
