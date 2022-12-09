from class_tracker import CryptoTracker

# Setup class
crypto_tracker = CryptoTracker()

# Test class
symbol_in = "BTC"
start_date = "2022-10-30"
print(crypto_tracker.aud_trades(symbol_in, start_date)["Cost"].sum())