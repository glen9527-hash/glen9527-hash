import streamlit as st
import requests
from datetime import datetime

# 網頁標題
st.set_page_config(page_title="📈 加密貨幣分析助手（Beta）")

# 頁面標題
st.title("📈 加密貨幣分析助手（Beta）")
st.markdown("**分析週期：1小時｜追蹤幣種：BTC / ETH / SOL**")

# 幣種 ID 對照（符合 Coingecko API）
COIN_MAPPING = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana"
}

# 獲取幣價（使用 Coingecko 免費 API）
def get_price(symbol):
    coin_id = COIN_MAPPING.get(symbol)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[coin_id]["usd"]
        else:
            return None
    except Exception as e:
        return None

# 顯示幣價
for symbol in ["BTC", "ETH", "SOL"]:
    price = get_price(symbol)
    if price is not None:
        st.success(f"{symbol} 現價：${price}")
    else:
        st.error(f"無法獲取 {symbol} 價格")

# 顯示更新時間
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.caption(f"更新時間：{now}")
