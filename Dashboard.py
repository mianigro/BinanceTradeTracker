import streamlit as st
from class_tracker import CryptoTracker

# Instantiate the class
crypto_tracker = CryptoTracker()

# Setup page
st.title("Binance Crypto Tracker")
st.subheader("View your trade history.")
