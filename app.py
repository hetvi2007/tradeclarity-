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
    st.write(f"**Market Cap**: ₹ {info.get('marketCap', 'N/A')}")
    st.write(f"**52-Week High / Low**: ₹ {info.get('fiftyTwoWeekHigh', 'N/A')} / ₹ {info.get('fiftyTwoWeekLow', 'N/A')}")
    st.write(f"**PE Ratio**: {info.get('trailingPE', 'N/A')}")
    st.write(f"**Dividend Yield**: {info.get('dividendYield', 'N/A')}")

with tab2:
    st.subheader("📈 Last 6 Months Price Chart")
    st.line_chart(history["Close"])

with tab3:
    st.subheader("💡 Suggestion Based on 52-Week Range")

    current = info.get("currentPrice", None)
    high = info.get("fiftyTwoWeekHigh", None)
    low = info.get("fiftyTwoWeekLow", None)

    if current and high and low:
        percentage = ((current - low) / (high - low)) * 100

        if percentage < 35:
            st.success("🟢 This stock seems **undervalued** right now. Consider **Buying**.")
        elif percentage > 80:
            st.warning("🔴 This stock is near its peak. Might be a **Sell** opportunity.")
        else:
            st.info("🟡 This stock is trading in a neutral zone. Consider **Holding** or watching.")

    else:
        st.error("❌ Not enough data to generate suggestion.")

st.caption("Made for Gen Z – by Ayush, for Aavashkar ✨")
