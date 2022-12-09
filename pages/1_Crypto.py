import pandas as pd
import numpy as np
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from class_tracker import CryptoTracker

# Instantiate the class
crypto_tracker = CryptoTracker()

# Setup page
st.title("Crypto Tracker - AUD")
st.subheader("View your trade history.")

# Sidebar with use input
st.sidebar.header("Crypto Price Tracker")
crypto_name = st.sidebar.text_input("Crypto Name")
start_date = st.sidebar.date_input("Start date")
start_date = start_date.strftime("%Y-%m-%d")
get_currency = st.sidebar.button("Get Trade Info")
get_profit = st.sidebar.button("Get Profit Info")
get_units = st.sidebar.button("Get Unit Info")
get_ave_price = st.sidebar.button("Get Average Prices")

# Results on button press
if get_currency:
    trades_out = crypto_tracker.aud_trades(crypto_name, start_date).reset_index()

    # Display dataframe of trades
    st.dataframe(trades_out)

    # Download
    trade_csv = trades_out.to_csv()
    st.download_button(
        label="Download Data",
        data=trade_csv,
        file_name=f"{crypto_name}_trade_data.csv",
        mime="text/csv"
    )

if get_profit:
    trades_out = crypto_tracker.aud_trades(crypto_name, start_date).reset_index()

    # Display profit graph
    fig, ax = plt.subplots()
    ax.plot(trades_out["Cost"].cumsum())
    ax.set_xlabel("Trade Number")
    ax.set_ylabel("Net Change")
    st.pyplot(fig)

if get_units:
    trades_out = crypto_tracker.aud_trades(crypto_name, start_date).reset_index()

    # Getting unit information
    trades_out["Units Net"] = np.where(trades_out["Type"] == "Buy", trades_out["Units"], -1 * trades_out["Units"])

    fig, ax = plt.subplots()
    ax.plot(trades_out["Units Net"].cumsum())
    ax.set_xlabel("Trade Number")
    ax.set_ylabel("Net Change Units")
    st.pyplot(fig)


if get_ave_price:
    trades_out = crypto_tracker.aud_trades(crypto_name, start_date).reset_index()
    average_buy = trades_out["Price"][trades_out["Type"] == "Buy"].mean()
    st.subheader(f"Price Buy Price: ${average_buy}")

    average_sell = trades_out["Price"][trades_out["Type"] == "Sell"].mean()
    st.subheader(f"Price Sell Price: ${average_sell}")

