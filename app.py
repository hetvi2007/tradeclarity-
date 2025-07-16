import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Custom dark theme with neon highlights
st.markdown("""
    <style>
    body, .stApp {
        background-color: #000;
        color: #39ff14;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, .stTextInput label, .stSelectbox label, .stMarkdown {
        color: #39ff14 !important;
    }
    .stTextInput > div > div > input {
        background-color: #111 !important;
        color: #39ff14 !important;
        border: 1px solid #39ff14;
    }
    .stButton>button {
        background-color: #000;
        color: #39ff14;
        border: 1px solid #39ff14;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #39ff14;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("📊 TradeClarity")
st.subheader("Helping Gen Z make smarter trading decisions 💡")

# Input: Stock symbol
symbol = st.text_input("Enter Stock Symbol (e.g._
