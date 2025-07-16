import streamlit as st
import yfinance as yf

st.set_page_config(page_title="TradeClarity", page_icon="📈", layout="centered")

st.title("📊 TradeClarity – Make Smart Trading Moves")
st.markdown("Empowering Gen Z to trade confidently with clear, no-jargon insights.")

# Stock choices
stocks = {
    "Apple Inc (AAPL)": "AAPL",
    "Tesla Motors (TSLA)": "TSLA",
    "Infosys Ltd (INFY.NS)": "INFY.NS",
    "Reliance Industries (RELIANCE.NS)": "RELIANCE.NS",
    "TCS (TCS.NS)": "TCS.NS",
    "HDFC Bank (HDFCBANK.NS)": "HDFCBANK.NS",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL"
}

choice = st.selectbox("📌 Select a Stock", list(stocks.keys()))
ticker = stocks[choice]

# Load stock data
stock = yf.Ticker(ticker)
info = stock.info
history = stock.history(period="6mo")

# Tabs
tab1, tab2, tab3 = st.tabs(["📄 Overview", "📈 Price Chart", "💹 Buy/Sell Suggestion"])

with tab1:
    st.subheader(f"{info.get('longName', ticker)}")
    st.write(f"**Exchange**: {info.get('exchange', 'N/A')}")
    st.write(f"**Sector**: {info.get('sector', 'N/A')}")
    st.write(f"**Current Price**: ₹ {info.get('currentPrice', 'N/A')}")
    st.write(f"**Market Cap**: ₹ {
