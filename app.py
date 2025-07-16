import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

st.set_page_config(page_title="TradeClarity", layout="wide")
st.markdown("<h1 style='color:#00bfff;'>📊 TradeClarity</h1>", unsafe_allow_html=True)

# Full name to symbol mapping for NSE
nse_stocks = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys Ltd": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS",
    "Kotak Mahindra Bank": "KOTAKBANK.NS",
    "ITC Ltd": "ITC.NS",
    "Larsen & Toubro": "LT.NS",
    "Axis Bank": "AXISBANK.NS",
    "Hindustan Unilever": "HINDUNILVR.NS",
    "Bajaj Finance": "BAJFINANCE.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "Asian Paints": "ASIANPAINT.NS",
    "HCL Technologies": "HCLTECH.NS",
    "Wipro Ltd": "WIPRO.NS",
    "Sun Pharma": "SUNPHARMA.NS",
    "Power Grid Corporation": "POWERGRID.NS",
    "Titan Company": "TITAN.NS",
    "UltraTech Cement": "ULTRACEMCO.NS"
    # You can add more here
}

# US stocks and BSE for future use
us_stocks = {
    "Technology": ["AAPL", "MSFT", "GOOGL", "NVDA"],
    "Healthcare": ["JNJ", "PFE", "MRK", "ABT"],
    "Financials": ["JPM", "BAC", "WFC", "GS"],
    "Energy": ["XOM", "CVX", "BP", "TOT"]
}

st.sidebar.title("🔎 Select Market, Sector & Stock")
selected_market = st.sidebar.selectbox("Choose Market", ["NSE", "US"])

if selected_market == "US":
    selected_sector = st.sidebar.selectbox("Choose Sector", list(us_stocks.keys()))
    symbol_list = us_stocks[selected_sector]
    selected_symbol = st.sidebar.selectbox("Choose Stock", symbol_list)
else:
    selected_company = st.sidebar.selectbox("Choose Stock", list(nse_stocks.keys()))
    selected_symbol = nse_stocks[selected_company]

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
fig.update_layout(
    title=f"{selected_symbol} - 6 Month Candlestick Chart",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_dark"
)

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
        market_cap = info.get('marketCap')
        st.metric("Market Cap", f"₹ {market_cap:,}" if market_cap else "N/A")
        st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")

with tabs[1]:
    st.plotly_chart(fig, use_container_width=True)

with tabs[2]:
    st.info("📈 Prediction features coming soon!")

with tabs[3]:
    st.info("📰 News integration coming soon!")
