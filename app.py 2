import streamlit as st
import yfinance as yf
from datetime import date, timedelta

# ----------------- PAGE CONFIG ----------------- #
st.set_page_config(
    page_title="TradeClarity",
    page_icon="📈",
    layout="centered"
)

# ----------------- HEADER ----------------- #
st.title("📊 TradeClarity")
st.caption("Gen Z’s guide to smarter trading 💡")

st.markdown("""
Welcome to **TradeClarity** – a lightweight, beginner-friendly stock insight tool made *for Gen Z, by Gen Z*.  
Check charts, explore trends, and avoid beginner mistakes in style.
""")

# ----------------- USER INPUT ----------------- #
ticker = st.text_input("🔍 Enter a stock symbol (e.g., AAPL, TSLA, TCS):", "AAPL")

# ----------------- DATE RANGE ----------------- #
end = date.today()
start = end - timedelta(days=30)

# ----------------- FETCH DATA ----------------- #
if ticker:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start, end=end)

        if not hist.empty:
            st.subheader(f"📅 Last 30 Days: {ticker.upper()}")
            st.line_chart(hist["Close"])

            st.subheader("📉 Key Stats")
            info = stock.info
            st.write({
                "Current Price": info.get("currentPrice", "N/A"),
                "52-Week High": info.get("fiftyTwoWeekH
