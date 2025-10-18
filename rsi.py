import yfinance as yf
import pandas as pd
import ta
import os
import requests

# 1️⃣ QQQ 데이터 다운로드 (최근 6개월치 주봉 데이터)
data = yf.download("QQQ", period="6mo", interval="1wk")
# data = yf.download("QQQ", period="6mo")

# 2️⃣ RSI 계산 (14기간 기준)
data["RSI"] = ta.momentum.RSIIndicator(data["Close"]["QQQ"], window=14).rsi()

# 3️⃣ 최신 데이터 확인
# 인덱스는 주말 기준으로 표시됨 (금요일 종가)
print(data.tail(10))

# 4️⃣ 지지난주와 지난주의 RSI 추출
# -1: 가장 최근 주 (이번주)
# -2: 지난주
# -3: 지지난주
rsi_last_week = data["RSI"].iloc[-2]
rsi_prev_week = data["RSI"].iloc[-3]

file_name = "mode.txt"
if os.path.exists(file_name):
    mode = open(file_name).read()
else:
    mode = "안전"

if rsi_last_week < rsi_prev_week and (
    rsi_last_week >= 65
    or (rsi_last_week >= 40 and rsi_last_week <= 50)
    or (rsi_prev_week >= 50 and rsi_last_week < 50)
):
    mode = "안전"
elif rsi_last_week > rsi_prev_week and (
    rsi_last_week <= 35
    or (rsi_last_week >= 50 and rsi_last_week >= 60)
    or (rsi_prev_week <= 50 and rsi_last_week > 50)
):
    mode = "공세"

message = f"""
동파 모드 알리미
지지난주 RSI: {rsi_prev_week:.2f}
지난주 RSI: {rsi_last_week:.2f}
모드: {mode}
"""

with open(file_name, "w") as f:
    f.write(mode)


def send_telegram_message(message):
    TOKEN = "6639060776:AAH2I1xEeHTzlwl3KZkPW-n4ciTfGBAOoN4"  # 🔸 텔레그램 봇 토큰 입력
    CHAT_ID = "5139435283"  # 🔸 수신할 채팅 ID 입력
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
        print("📨 텔레그램 메시지 전송 완료")
    except Exception as e:
        print("❌ 텔레그램 전송 실패:", e)


print(message)
send_telegram_message(message)
