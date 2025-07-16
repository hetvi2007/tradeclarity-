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

# ✅ FIXED: closed the string properly here
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, INFY)", "AAPL")

if symbol:
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period="6mo")

        st.subheader(f"Stock Chart for {symbol.upper()}")
        fig, ax = plt.subplots()
        ax.plot(hist.index, hist["Close"], color="#39ff14")
        ax.set_facecolor("#000")
        fig.patch.set_facecolor("#000")
        ax.tick_params(colors='#39ff14')
        ax.spines['bottom'].set_color('#39ff14')
        ax.spines['left'].set_color('#39ff14')
        st.pyplot(fig)

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
        st.error("⚠️ Could not load stock data. Please check the symbol and try again.")
