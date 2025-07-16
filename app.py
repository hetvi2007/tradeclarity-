import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

# --- PAGE SETUP ---
st.set_page_config(page_title="TradeClarity", layout="wide")

# --- HEADER ---
st.markdown("<h1 style='color:cyan;'>📊 TradeClarity</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gray;'>Smarter stock insights for everyone</p>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Select Stock")
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g. AAPL, TCS.NS, INFY.NS)", "AAPL")

# Download data
today = date.today()
start_date = today - timedelta(days=365)

try:
    data = yf.download(symbol, start=start_date, end=today)
    info = yf.Ticker(symbol).info
except:
    st.error("Failed to fetch data. Please check the stock symbol.")
    st.stop()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📈 Overview", "📊 Chart", "🔮 Predictions (Coming Soon)"])

# --- OVERVIEW TAB ---
with tab1:
    st.subheader("Company Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Market Cap", f"₹ {info.get('marketCap', 'N/A'):,}")
        st.metric("Previous Close", f"₹ {info.get('previousClose', 'N/A')}")
    with col2:
        st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")
        st.metric("52-Week Low", f"₹ {info.get('fiftyTwoWeekLow', 'N/A')}")
    with col3:
        st.metric("PE Ratio", f"{info.get('trailingPE', 'N/A')}")
        st.metric("Dividend Yield", f"{info.get('dividendYield', 'N/A')}")

# --- CHART TAB ---
with tab2:
    st.subheader("Candlestick Chart")
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                increasing_line_color="cyan",
                decreasing_line_color="magenta"
            )
        ]
    )
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)

# --- PREDICTIONS TAB (Placeholder) ---
with tab3:
    st.info("Prediction tools coming soon! Stay tuned.")
