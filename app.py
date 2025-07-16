import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# App title
st.title("📊 TradeClarity")
st.subheader("Helping Gen Z make smarter trading decisions 💡")

# Stock symbol input
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, INFY)", "AAPL")

# Show stock data if input exists
if symbol:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period="6mo")

        # Stock chart
        st.subheader(f"Stock Chart for {symbol.upper()}")
        fig, ax = plt.subplots()
        ax.plot(hist.index, hist["Close"], color="blue")
        ax.set_title(f"{symbol.upper()} Price Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Close Price")
        st.pyplot(fig)

        # Stock Info
        st.subheader("Key Info")
        col1, col2 = st.columns(2)

        with col1
