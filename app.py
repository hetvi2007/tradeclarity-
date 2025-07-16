import streamlit as st
import yfinance as yf

# Page settings
st.set_page_config(page_title="TradeClarity", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📊 TradeClarity</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Your Gen Z companion to smarter trading 💸</h4>", unsafe_allow_html=True)
st.markdown("---")

# Input
ticker = st.text_input("🔎 Enter a stock ticker (e.g., AAPL, TSLA, INFY):")

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Company Name
        st.subheader(f"📘 {info.get('shortName', ticker)}")
        st.write(info.get("longBusinessSummary", "No summary available."))

        # Display Metrics in Columns
        col1, col2, col3 = st.columns(3)
        col1.metric("💵 Current Price", info.get("currentPrice", "N/A"))
        col2.metric("📈 52W High", info.get("fiftyTwoWeekHigh", "N/A"))
        col3.metric("📉 52W Low", info.get("fiftyTwoWeekLow", "N/A"))

        col4, col5 = st.columns(2)
        col4.metric("🏦 Market Cap", f"{info.get('marketCap', 'N/A'):,}")
        col5.metric("🧮 PE Ratio", info.get("trailingPE", "N/A"))

        # Divider
        st.markdown("---")

        # Historical Data Chart
        st.subheader("📅 Price Trend (Last 6 Months)")
        hist = stock.history(period="6mo")
        st.line_chart(hist["Close"])

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
else:
    st.info("Start by entering a stock symbol above ☝️")
