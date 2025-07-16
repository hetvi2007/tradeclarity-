import streamlit as st
import yfinance as yf

st.set_page_config(page_title="TradeClarity", layout="wide")

st.title("📈 TradeClarity – Smart Trading Insights for Gen Z")

st.write("Welcome! Enter a stock symbol below to get simplified, real-time data and make smarter trading decisions.")

# User input
ticker_symbol = st.text_input("🔍 Enter a Stock Symbol (e.g., AAPL, TSLA, INFY):")

if ticker_symbol:
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info

        st.subheader(f"📊 Snapshot: {info.get('shortName', ticker_symbol)}")
        
        st.write({
            "📌 Current Price": info.get("currentPrice", "N/A"),
            "📈 52-Week High": info.get("fiftyTwoWeekHigh", "N/A"),
            "📉 52-Week Low": info.get("fiftyTwoWeekLow", "N/A"),
            "💰 Market Cap": info.get("marketCap", "N/A"),
            "🧮 PE Ratio": info.get("trailingPE", "N/A")
        })

        st.markdown("---")
        st.subheader("📅 Price History (Last 6 Months)")

        hist = stock.history(period="6mo")
        st.line_chart(hist["Close"])

    except Exception as e:
        st.error(f"Something went wrong: {e}")
