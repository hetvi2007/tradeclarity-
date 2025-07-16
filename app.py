import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Custom Neon + Black Theme ---
st.markdown("""
<style>
.stApp {
    background-color: #0d0d0d;
    color: #39ff14;
}

html, body, [class*="css"] {
    font-family: 'Courier New', monospace;
    color: #39ff14;
}

h1, h2, h3, .st-bb, .st-at, .st-ae {
    color: #39ff14 !important;
    text-shadow: 0 0 10px #39ff14, 0 0 20px #39ff14;
}

div.stButton > button {
    background-color: #111;
    color: #39ff14;
    border: 1px solid #39ff14;
    border-radius: 8px;
    padding: 8px 20px;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #39ff14;
    color: black;
}

.css-1d391kg, .css-1dp5vir {
    background-color: #121212 !important;
    color: #39ff14;
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>🚀 <span style='color:#39ff14;'>TradeClarity</span></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Making Trading Fun, Smart & Gen Z Ready</h3>", unsafe_allow_html=True)

# --- Stock Input ---
st.markdown("""
### 🔍 Enter a stock symbol (e.g. `AAPL`, `TSLA`, `INFY.NS`, `TCS.NS`):
""")

stock_symbol = st.text_input("Stock Symbol", value="AAPL")

if stock_symbol:
    try:
        stock = yf.Ticker(stock_symbol)
        info = stock.info

        # --- Stock Info ---
        st.subheader(f"📈 Overview of {info.get('shortName', stock_symbol)}")
        st.write(f"**Market Cap**: ₹ {info.get('marketCap', 'N/A'):,}")
        st.write(f"**52-Week High**: ₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52-Week Low**: ₹ {info.get('fiftyTwoWeekLow', 'N/A')}")
        st.write(f"**PE Ratio**: {info.get('trailingPE', 'N/A')}")

        # --- Historical Data ---
        st.subheader("📊 Stock Price Chart")
        df = stock.history(period="6mo")

        plt.style.use("dark_background")
        fig, ax = plt.subplots()
        ax.plot(df.index, df['Close'], color='#39ff14', linewidth=2)
        ax.set_title(f"{stock_symbol} Closing Price", color='#39ff14')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        st.pyplot(fig)

    except Exception as e:
        st.error("Something went wrong! Check the stock symbol or try again.")
