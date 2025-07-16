import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# -------------------------------
# PAGE SETUP
# -------------------------------
st.set_page_config(
    page_title="TradeClarity",
    layout="wide",
)

st.title("📊 TradeClarity")
st.subheader("Helping everyone make smarter stock decisions")

# -------------------------------
# STOCK INPUT
# -------------------------------
symbol = st.text_input("Enter Stock Symbol (e.g., INFY.NS, TCS.NS, AAPL)", "TCS.NS")

if symbol:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        # -------------------------------
        # DATE RANGE SELECTION
        # -------------------------------
        timeframe = st.selectbox("Select Time Range", ["1W", "1M", "6M", "1Y", "5Y", "Max"])
        today = datetime.today()
        ranges = {
            "1W": today - timedelta(weeks=1),
            "1M": today - timedelta(days=30),
            "6M": today - timedelta(days=182),
            "1Y": today - timedelta(days=365),
            "5Y": today - timedelta(days=1825),
            "Max": datetime(2000, 1, 1)
        }
        start_date = ranges[timeframe]
        data = stock.history(start=start_date, end=today)

        # -------------------------------
        # CHART
        # -------------------------------
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['Close'],
            mode='lines',
            name='Close Price'
        ))
        fig.update_layout(
            title=f"{symbol.upper()} Price Chart ({timeframe})",
            xaxis_title="Date",
            yaxis_title="Price (INR)",
            template="plotly_white",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

        # -------------------------------
        # STOCK INFO
        # -------------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Market Cap", f"₹ {info.get('marketCap', 'N/A'):,}")
            st.metric("Previous Close", f"₹ {info.get('previousClose', 'N/A')}")
            st.metric("Open", f"₹ {info.get('open', 'N/A')}")
            st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")
            st.metric("52-Week Low", f"₹ {info.get('fiftyTwoWeekLow', 'N/A')}")

        with col2:
            st.metric("PE Ratio", info.get('trailingPE', 'N/A'))
            st.metric("EPS", info.get('trailingEps', 'N/A'))
            st.metric("Volume", f"{info.get('volume', 'N/A'):,}")
            st.metric("Dividend Yield", info.get('dividendYield', 'N/A'))
            st.metric("Exchange", info.get('exchange', 'N/A'))

    except Exception as e:
        st.error("Error fetching data. Please check the symbol or try again.")
else:
    st.info("Enter a stock symbol to begin.")
