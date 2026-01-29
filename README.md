# intraday_option_algo
# Intraday Options Algo - 3 Index

## Files

- data_fetcher.py → TrueData live tick data
- algo_engine.py → Trend, ATM strike, fake move, big player detection
- alert_runner.py → Telegram alerts
- main.py → Streamlit dashboard
- telegram_alert.py → Telegram sending function

## Run

1. Install requirements: pip install -r requirements.txt
2. Run Streamlit dashboard: streamlit run main.py
3. Run alerts in background: python alert_runner.py
