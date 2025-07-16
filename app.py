import streamlit as st
import yfinance as yf
import datetime

# Page config
st.set_page_config(page_title="TradeClarity", page_icon="📊", layout="centered")

st.markdown("""
    <div style="text-align:center">
        <h1 style="color:#6C63FF;">📊 TradeClarity</h1>
        <h4 style="color:gray;">Helping Gen Z make smarter trading decisions</h4>
        <hr style="border: 1px solid #ccc;">
    </div>
    """, unsafe_allow_html=True)

# Popular stock list
popular_stocks = {
    "Apple (AAPL)": "AAPL",
    "Google (GOOGL)": "GOOGL",
    "Amazon (AMZN)": "AMZN",
    "Tesla (TSLA)": "TSLA",
    "Microsoft (MSFT)": "MSFT",
    "Infosys (INFY)": "INFY.NS",
    "TCS (TCS)": "TCS.NS",
    "Reliance (RELIANCE)": "RELIANCE.NS",
    "HDFC Bank (HDFCBANK)": "HDFCBANK.NS",
    "ICICI Bank (ICICIBANK)": "ICICIBANK.NS"
}

# Selection method
st.markdown("### 🎯 Choose a stock or enter manually:")
selected = st.selectbox("Pick from popular stocks:", [""] + list(popular_stocks.keys()))
manual_input = st.text_input("Or type a stock symbol (e.g., AAPL, TCS.NS):").upper()

# Final ticker
ticker = ""
if selected:
    ticker = popular_stocks[selected]
elif manual_input:
    ticker = manual_input

# Process and display
if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        st.subheader(f"📈 {info.get('longName', ticker)}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("💵 Current Price", f"₹ {info.get('currentPrice', 'N/A')}")
            st.metric("📈 52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")
            st.metric("📉 52-Week Low", f"₹ {info.get('fiftyTwoWeekLow', 'N/A')}")

        with col2:
            st.metric("🏢 Market Cap", f"₹ {info.get('marketCap', 'N/A')}")
            st.metric("📊 Volume", f"{info.get('volume', 'N/A')}")
            st.metric("📐 PE Ratio", f"{info.get('trailingPE', 'N/A')}")

        st.subheader("📅 Stock Price Chart (Last 6 Months)")
        today = datetime.date.today()
        six_months_ago = today - datetime.timedelta(days=180)
        hist_data = stock.history(start=six_months_ago, end=today)

        if not hist_data.empty:
            st.line_chart(hist_data['Close'])
        else:
            st.warning("No chart data available for this stock.")

        st.caption("💡 This is not financial advice. Always do your own research!")

    except Exception as e:
        st.error(f"⚠️ Error loading data: {e}")
else:
    st.info("👆 Select or enter a stock symbol to continue.")

