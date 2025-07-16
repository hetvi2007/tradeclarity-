import streamlit as st
import yfinance as yf

st.set_page_config(page_title="TradeClarity", page_icon="📈", layout="centered")
st.title("📊 TradeClarity – Make Smart Trading Moves")
st.markdown("Empowering Gen Z to trade confidently with clear, no-jargon insights.")

# Dropdown
options = {
    "Apple Inc (AAPL)": "AAPL",
    "Tesla Motors (TSLA)": "TSLA",
    "Infosys Ltd (INFY.NS)": "INFY.NS",
    "Reliance Industries (RELIANCE.NS)": "RELIANCE.NS",
    "TCS (TCS.NS)": "TCS.NS",
    "HDFC Bank (HDFCBANK.NS)": "HDFCBANK.NS",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL"
}

selected = st.selectbox("Choose a company:", list(options.keys()))
ticker = options[selected]
stock = yf.Ticker(ticker)
info = stock.info
hist = stock.history(period="6mo")

# Tabs
tab1, tab2 = st.tabs(["📄 Overview", "📈 Price Chart"])

with tab1:
    st.subheader(f"{info.get('longName', ticker)}")
    st.write(f"**Exchange**: {info.get('exchange', 'N/A')}")
    st.write(f"**Sector**: {info.get('sector', 'N/A')}")
    st.write(f"**Current Price**: ₹ {info.get('currentPrice', 'N/A')}")
    st.write(f"**Market Cap**: ₹ {info.get('marketCap', 'N/A')}")
    st.write(f"**52-Week High / Low**: ₹ {info.get('fiftyTwoWeekHigh', 'N/A')} / ₹ {info.get('fiftyTwoWeekLow', 'N/A')}")
    st.write(f"**PE Ratio**: {info.get('trailingPE', 'N/A')}")
    st.write(f"**Dividend Yield**: {info.get('dividendYield', 'N/A')}")

with tab2:
    st.line_chart(hist['Close'])

