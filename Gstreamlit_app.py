import streamlit as st
import requests

st.set_page_config(page_title="Crypto AI 助手", layout="centered")

st.title("📈 加密貨幣 AI 分析建議")
st.write("正在獲取 BTC、ETH、SOL 的行情資訊...")

# 示例價格模擬（可改為接入 API）
prices = {
    "BTC": 64250,
    "ETH": 3400,
    "SOL": 168.3
}

# 示例建議
suggestions = {
    "BTC": "1H RSI 過熱，建議觀望或高位做空，止損：65000，止盈：62300。",
    "ETH": "新聞面中性，技術指標偏弱，建議保守觀望。",
    "SOL": "資金費率轉負，1H KDJ 死叉，建議輕倉空單，止損：170.5，止盈：163.2。"
}

for coin in prices:
    st.subheader(f"💰 {coin} 現價：{prices[coin]} USDT")
    st.write(suggestions[coin])
