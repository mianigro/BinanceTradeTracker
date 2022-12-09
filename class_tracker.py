from binance.client import Client
from dotenv import load_dotenv
import os
import numpy as np
import pandas as pd
from datetime import datetime


class CryptoTracker:
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('KEY')
        self.secret = os.getenv('SECRET')
        self.client = Client(self.key, self.secret)

    def aud_trades(self, crypto_symbol, start_date):
        # Get trades
        pair_trades = self.client.get_my_trades(symbol=f"{crypto_symbol}AUD")
        start_date = datetime.strptime(start_date, '%Y-%m-%d')

        # Loop pair 1 trades
        all_trades = []
        for item in pair_trades:
            if datetime.fromtimestamp(int(item["time"]) / 1000) >= start_date:
                if item["isBuyer"]:
                    all_trades.append(
                        {"Trade ID": item["id"], "Type": "Buy", "Symbol": item["symbol"], "Units": item["qty"],
                         "Price": item["price"], "Commission Asset": item["commissionAsset"],
                         "Commission Units": item["commission"]})
                else:
                    all_trades.append(
                        {"Trade ID": item["id"], "Type": "Sell", "Symbol": item["symbol"], "Units": item["qty"],
                         "Price": item["price"], "Commission Asset": item["commissionAsset"],
                         "Commission Units": item["commission"]})

        trades_df = pd.DataFrame(
            all_trades,
            columns=["Trade ID", "Type", "Symbol", "Units", "Price",
                     "Commission Asset", "Commission Units"]).set_index("Trade ID")

        trades_df["Units"] = trades_df["Units"].astype("float32")
        trades_df["Price"] = trades_df["Price"].astype("float32")

        trades_df["Cost"] = np.where(trades_df["Type"] == "Buy",
                                     -1 * trades_df["Units"] * trades_df["Price"],
                                     trades_df["Units"] * trades_df["Price"])

        return trades_df

    def pair_trades(self, crypto_pair, start_date):
        # Get trades
        pair_trades = self.client.get_my_trades(symbol=crypto_pair)
        start_date = datetime.strptime(start_date, '%Y-%m-%d')

        # Loop pair 1 trades
        all_trades = []
        for item in pair_trades:
            if datetime.fromtimestamp(int(item["time"]) / 1000) >= start_date:
                if item["isBuyer"]:
                    all_trades.append(
                        {"Trade ID": item["id"], "Type": "Buy", "Symbol": item["symbol"], "Units": item["qty"],
                         "Price": item["price"], "Commission Asset": item["commissionAsset"],
                         "Commission Units": item["commission"]})
                else:
                    all_trades.append(
                        {"Trade ID": item["id"], "Type": "Sell", "Symbol": item["symbol"], "Units": item["qty"],
                         "Price": item["price"], "Commission Asset": item["commissionAsset"],
                         "Commission Units": item["commission"]})

        trades_df = pd.DataFrame(
            all_trades,
            columns=["Trade ID", "Type", "Symbol", "Units", "Price",
                     "Commission Asset", "Commission Units"]).set_index("Trade ID")

        trades_df["Units"] = trades_df["Units"].astype("float32")
        trades_df["Price"] = trades_df["Price"].astype("float32")

        trades_df["Cost"] = np.where(trades_df["Type"] == "Buy",
                                     -1 * trades_df["Units"] * trades_df["Price"],
                                     trades_df["Units"] * trades_df["Price"])

        return trades_df
