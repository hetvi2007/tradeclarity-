import streamlit as st
import yfinance as yf

st.set_page_config(page_title="TradeClarity", page_icon="📈", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>📊 TradeClarity</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: gray;'>Helping Gen Z make smarter trading decisions</h4><hr>",
    unsafe_allow_html=True
)

# Select stock
stocks = {
    "Apple Inc (AAPL)": "AAPL",
    "Tesla Motors (TSLA)": "TSLA",
    "Infosys Ltd (INFY.NS)": "INFY.NS",
    "Reliance Industries (RELIANCE.NS)": "RELIANCE.NS",
    "TCS (TCS.NS)": "TCS.NS",
    "HDFC Bank (HDFCBANK.NS)": "HDFCBANK.NS",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL"
}
c
