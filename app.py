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
        st.error("⚠️ Could not load stock data. Please check the symbol and your internet connection.")
