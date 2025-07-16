import streamlit as st
import yfinance as yf
import datetime

# Page config
st.set_page_config(page_title="TradeClarity", page_icon="📊", layout="centered")

# Stylish title section
st.markdown("""
    <div style="text-align:center">
        <h1 style="color:#6C63FF;">📊 TradeClarity</h1>
        <h4 style="color:gray;">Helping Gen Z make smarter trading decisions</h4>
        <hr style="border: 1px solid #ccc;">
    </div>
    """, unsafe_allow_html=True)

# Input for stock ticker
ticker = st.text_input("🔍 Enter a Stock Symbol (e.g. AAPL, INFY, TATASTEEL):").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Display stock overview
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

        # Show chart
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
    st.info("👆 Enter a stock symbol to get started.")
