import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="📈 加密貨幣分析助手（Beta）")
st.title("📈 加密貨幣分析助手（Beta）")
st.markdown("**分析週期：1小時｜追蹤幣種：BTC / ETH / SOL**")

# CoinCap 對應名稱
SYMBOLS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana"
}

# 使用 CoinCap API
def get_price(symbol):
    try:
        url = f"https://api.coincap.io/v2/assets/{symbol}"
        r = requests.get(url, timeout=10)
        data = r.json()
        return float(data["data"]["priceUsd"])
    except Exception as e:
        return None

# 顯示價格
for short_symbol, api_symbol in SYMBOLS.items():
    price = get_price(api_symbol)
    if price:
        st.success(f"{short_symbol} 現價：${price:,.2f}")
    else:
        st.error(f"無法獲取 {short_symbol} 價格")

# 更新時間
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.caption(f"更新時間：{now}")
