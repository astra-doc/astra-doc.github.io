import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from dotenv import dotenv_values


def get_soxl_rsi(period="14", interval="1d", lookback=100):
    ticker = yf.Ticker("SOXL")
    data = ticker.history(period=f"{lookback}d", interval=interval)
    if data.empty:
        raise ValueError("SOXL 데이터를 가져오지 못했습니다.")
    print(data["Close"])
    rsi = RSIIndicator(close=data["Close"], window=int(period)).rsi()
    current_rsi = rsi.iloc[-1]
    return round(current_rsi, 2)


print(get_soxl_rsi())
