import streamlit as st
import yfinance as yf
import datetime

# 🎨 Page Configuration
st.set_page_config(page_title="TradeClarity", page_icon="📊", layout="centered")

# 🟣 Stylish Title Section
st.markdown(
    """
    <div style="text-align:center">
        <h1 style="color:#6C63FF; font-size: 3em;">📊 TradeClarity</h1>
        <h4 style="color:gray;">Helping Gen Z make smarter trading decisions</h4>
        <hr style="border: 1px solid #ccc;">
    </div>
    """,
    unsafe_allow_html=True
)

# 🔍 Ticker Input
ticker = st.text_input("Enter a Stock Symbol (like AAPL, INFY, TATASTEEL):").upper()

if ticker:
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        st.subheader(f"📈 {info.get('longName', ticker)} Overview")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Price", f"₹ {info.get('currentPrice', 'N/A')}")
            st.metric("52-Week High", f"₹ {info.get('fiftyTwoWeekHigh', 'N/A')}")
            st.metric("52-Week Low", f"₹ {info.get('fiftyTwoWeekLow', 'N/A')}")

        with col2:
            st.metric("Market Cap", f"₹ {info.get('marketCap', 'N/A')}")
            st.metric("Volume", f"{info.get('volume', 'N/A')}")
            st.metric("PE Ratio", f"{info.get('trailingPE', 'N/A')}")

        # 📅 Date range for historical data
        st.subheader("📅 Stock Price Chart")
        today = datetime.date.today()
        past = today - datetime.timedelta(days=180)
        df = stock.history(start=past, end=today)

        st.line_chart(df['Close'])

        # 💡 Suggestive Text
        st.info("Tip: This is not financial advice. Always DYOR – Do Your Own Research!")

    except Exception as e:
        st.error("⚠️ Could not fetch data. Make sure the symbol is correct.")

# 🎨 Footer
st.markdown("<hr><center><small>Built with ❤️ using Streamlit</small></center>", unsafe_allow_html=True)
