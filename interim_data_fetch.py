import requests
import pandas as pd
import json
import csv
import io
from tkinter import *
import tkinter as tk
#---- constants-------------------------------#
API_KEY = "K1AXX01WY0BSF8YV"
BASE_URL = "https://www.alphavantage.co/query"
FUNCTION_TIME_SERIES = "TIME_SERIES_INTRADAY"
SYMBOL = "eurusd"
INTERVAL = "5min"
TIME_PERIOD_SHORT = "20"
TIME_PERIOD_MEDIUM = "90"
TIME_PERIOD_LONG = "200"
OUTPUTSIZE = "full"
SERIES_TYPE = "open"
MONTH= "2024-11"


def data_extract():
	parameters_intra_day = {
		"function":FUNCTION_TIME_SERIES,
		"symbol": SYMBOL,
		"interval": INTERVAL,
		"outputsize": OUTPUTSIZE,
		"series_type": "open",
		"apikey":API_KEY,
	}

	indicator_functions = ["SMA", "EMA", "DEMA"]

	for function in indicator_functions:
		technical_indicator = function
		parameters_indicators = {
			"function": technical_indicator,
			"symbol": SYMBOL,
			"interval": INTERVAL,
			"time_period": TIME_PERIOD_SHORT,
			"outputsize":OUTPUTSIZE,
			"series_type": "open",
			"apikey":API_KEY,
		}
		response = requests.get(BASE_URL, params=parameters_indicators)
		data = response.json()
		with open(f"response_{technical_indicator}", 'w') as json_file:
			json.dump(data, json_file, indent=4)

		df = pd.read_json("response.json")
		df.to_csv(f"{SYMBOL}_{technical_indicator}.csv", index=False)
		df.index.name = 'timestamp'
		df.reset_index(inplace=True)

		print(f"Downloaded {technical_indicator} data for {SYMBOL}")
    # time_period = ""

    # def fetch_price_data(self):
    #     """fetches price data based on user request for the past 30 days"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}& & month= 2024-03 & outputsize=full&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"./csv_file_repository/{symbol}_{function}.csv", index=False)
    #
    #
    #
    # def fetch_rsi():
    #     """fetches relative strength index based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_sma():
    #     """fetches simple moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_ema():
    #     """fetches exponential moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_wma():
    #     """fetches weighted moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_dema():
    #     """fetches double exponential moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_tema():
    #     """fetches triple exponential moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_trima():
    #     """fetches triangular moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_mama():
    #     """fetches MESA moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&fastlimit = 0.02&apikey={API_KEY}"
    #
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_kama():
    #     """fetches Kaufman moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_vmap():
    #     """fetches volume weighted average price based on user request in this settig only calculatingon the last 30 days"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_t3():
    #     """fetches triple exponential moving average based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # #--- not ready to do this yet
    # def fetch_macdext():
    #     pass
    #
    # def fetch_stoch():
    #     """fetches stochastic oscillator based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_stochf():
    #     """fetches stochastic fast oscillator based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_stochrsi():
    #     """fetches stochastic relative strength index based on user request"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type=open& fastkperiod = 6 & fastdmatype = 1&apikey={API_KEY}"
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_willr():
    #     """fetches Williams' %R based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_adx():
    #     """fetches average directional movement index  based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_adxr():
    #     """fetches average directional movement index rating based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    #
    # def fetch_apo():
    #     """fetches absolute price oscillator based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&series_type = close & fastperiod = 10 & matype = 1 &apikey={API_KEY}"
    #
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_mfi():
    #     """fetches money flow index based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_atr():
    #     """fetches average true range based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
    # def fetch_obv():
    #     """fetches on balance volume based on user request with default settings"""
    #     url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&time_period={time_period}&apikey={API_KEY}"
    #
    #     response = requests.get(url)
    #     data = response.json()
    #     with open("response.json", 'w') as json_file:
    #         json.dump(data, json_file, indent=4)
    #
    #     df = pd.read_json("response.json")
    #     df.to_csv(f"{symbol}_{function}.csv", index=False)
    #
