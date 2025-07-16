import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

st.set_page_config(page_title="TradeClarity", layout="wide")

st.markdown("<h1 style='color:#00bfff;'>📊 TradeClarity</h1>", unsafe_allow_html=True)

# Define sectors and related stocks (expanded list)
sectors = {
    "Technology": ["AAPL", "MSFT", "GOOGL", "NVDA", "AMD", "INTC", "CRM", "ORCL"],
    "Healthcare": ["JNJ", "PFE", "MRK", "ABT", "UNH", "LLY", "BMY", "CVS"],
    "Financials": ["JPM", "BAC", "WFC", "GS", "MS", "C", "AXP", "BLK"],
    "Energy": ["XOM", "CVX", "BP", "TOT", "COP", "PSX", "EOG", "SLB"],
    "Consumer Discretionary": ["AMZN", "TSLA", "HD", "MCD", "NKE", "SBUX", "LOW", "TGT"],
    "Industrials": ["BA", "CAT", "GE", "MMM", "HON", "LMT", "UPS", "FDX"]
}

st.sidebar.title("🔎 Select Sector & Stock")
selected_sector = st.sidebar.selectbox("Choose Sector", list(sectors.keys()))
symbol_list = sectors[selected_sector]
selected_symbol = st.sidebar.selectbox("Choose Stock", symbol_list)

# Fetch data
ticker = yf.Ticker(selected_symbol)
data = ticker.history(period="6mo")
info = ticker.info

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name="Candlestick"
)])
fig.update_layout(title=f"{selected_symbol} - 6 Month Candlestick Chart", xaxis_title="Date", yaxis_title="Price (INR)", template="plotly_dark")

# Layout with tabs
tabs = st.tabs(["Overview", "Chart", "Predictions (Coming Soon)", "News (Coming Soon)"])

with tabs[0]:
    st.subheader(f"Overview: {selected_symbol}")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Previous Close", f"₹ {info.get('previousClose', 'N/A')}")
        st.metric("Open", f"₹ {info.get('open', 'N/A')}")
    with col2:
        st.metric("Day High", f"₹ {info.get('dayHigh', 'N/A')}")
        st.metric("Day Low", f"₹ {info.get('dayLow', 'N/A')}")
    with col3:
        st.metric("Market Cap", f"₹ {info.get('marketCap', 'N/A'):,}" if info.get('marketCap') else "N/A")
        st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")

with tabs[1]:
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    st.info("📈 Prediction features coming soon!")

with tabs[3]:
    st.info("📰 News integration coming soon!")
