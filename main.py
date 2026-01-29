# main.py
import streamlit as st
from data_fetcher import live_data
from algo_engine import get_atm_strike, get_trend
import numpy as np

st.title("Intraday Options Algo Dashboard")

symbols = ["NIFTY-I","BANKNIFTY-I","SENSEX-I"]
selected_symbol = st.selectbox("Select Index", symbols)

data = live_data.get(selected_symbol, {})

if data:
    spot = data['ltp']
    gap = 50 if selected_symbol != "BANKNIFTY-I" else 100
    atm = get_atm_strike(spot, gap)

    # Simplified trend calculation
    ltp_list = [spot]
    vwap = np.mean(ltp_list)
    ema20 = np.mean(ltp_list)
    ema50 = np.mean(ltp_list)
    trend = get_trend(spot, vwap, ema20, ema50)

    st.write(f"Spot: {spot}")
    st.write(f"ATM Strike: {atm}")
    st.write(f"Trend: {trend}")
else:
    st.write("Waiting for TrueData ticks...")
