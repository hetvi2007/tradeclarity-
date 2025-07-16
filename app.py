import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# ----- PAGE CONFIG -----
st.set_page_config(page_title="TradeClarity", layout="wide")

# ----- HEADER -----
st.markdown("<h1 style='color:#4A90E2;'>📊 TradeClarity</h1>", unsafe_allow_html=True)

# ----- STOCK SELECTION -----
stock_options = {
    "Apple Inc. (AAPL)": "AAPL",
    "Tesla Inc. (TSLA)": "TSLA",
    "Amazon.com Inc. (AMZN)": "AMZN",
    "Microsoft Corporation (MSFT)": "MSFT",
    "Google (Alphabet Inc. - GOOGL)": "GOOGL",
    "NVIDIA Corporation (NVDA)": "NVDA",
    "Reliance Industries (RELIANCE.NS)": "RELIANCE.NS",
    "Tata Consultancy Services (TCS.NS)": "TCS.NS",
    "Infosys Limited (INFY.NS)": "INFY.NS",
    "HDFC Bank Limited (HDFCBANK.NS)": "HDFCBANK.NS"
}

selected_company = st.selectbox("📈 Choose a Stock", list(stock_options.keys()))
symbol = stock_options[selected_company]

# ----- FETCH DATA -----
ticker = yf.Ticker(symbol)
info = ticker.info

df = ticker.history(period="6mo")

# ----- TABS -----
tab1, tab2 = st.tabs(["📊 Overview", "📉 Chart"])

# ----- OVERVIEW -----
with tab1:
    st.subheader(f"{selected_company} - Stock Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Previous Close", f"₹ {info.get('previousClose', 'N/A'):,}")
        st.metric("Open", f"₹ {info.get('open', 'N/A'):,}")
    with col2:
        st.metric("Day's High", f"₹ {info.get('dayHigh', 'N/A'):,}")
        st.metric("Day's Low", f"₹ {info.get('dayLow', 'N/A'):,}")
    with col3:
        market_cap = info.get('marketCap')
        st.metric("Market Cap", f"₹ {market_cap:,}" if market_cap else "N/A")
        st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A'):,}")
        st.metric("52-Week Low", f"₹ {info.get('fiftyTwoWeekLow', 'N/A'):,}")

# ----- CHART -----
with tab2:
    st.subheader(f"{symbol} - Candlestick Chart (6M)")
    
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name=symbol
    )])
    
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        template="plotly_white",
        margin=dict(t=20, b=20),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
