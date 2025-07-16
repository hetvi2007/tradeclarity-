import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Inject custom CSS for dark theme with neon text
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #39ff14;
    }
    .stApp {
        background-color: #000000;
        color: #39ff14;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3 {
        color: #39ff14;
    }
    .css-1d391kg, .css-hxt7ib {
        background-color: #111111;
        color: #39ff14;
        border: 1px solid #39ff14;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>📊 TradeClarity</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Helping Gen Z make smarter trading decisions 💸</h3>", unsafe_allow_html=True)
st.markdown("---")

# Stock input
stock = st.text_input("🔍 Enter Stock Symbol (like AAPL, TSLA, INFY):", value="AAPL")

# Fetch data
if stock:
    try:
        data = yf.Ticker(stock)
        hist = data.history(period="6mo")

        # Chart
        st.subheader(f"📈 Stock Price Chart for {stock.upper()}")
        fig, ax = plt.subplots()
        ax.plot(hist.index, hist["Close"], color="#39ff14")
        ax.set_facecolor("#000000")
        fig.patch.set_facecolor('#000000')
        ax.tick_params(colors='white')
        st.pyplot(fig)

        # Stock Info
        st.subheader("📌 Stock Snapshot")
        info = data.info
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Name**: {info.get('shortName', 'N/A')}")
            st.write(f"**Sector**: {info.get('sector', 'N/A')}")
            st.write(f"**Market Cap**: ₹ {info.get('marketCap', 'N/A')}")
            st.write(f"**52-Week High**: ₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")

        with col2:
            st.write(f"**Previous Close**: ₹ {info.get('previousClose', 'N/A')}")
            st.write(f"**Open**: ₹ {info.get('open', 'N/A')}")
            st.write(f"**Volume**: {info.get('volume', 'N/A')}")
            st.write(f"**PE Ratio**: {info.get('trailingPE', 'N/A')}")

    except Exception as e:
        st.error("⚠️ Could not fetch data. Please check the stock symbol and try again.")
