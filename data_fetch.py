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

FONT = "Helvetica"
BACKGROUND_COLOR = "#091057"
HEADER_COLOR = "#024CAA"
BODY_COLOR = "#DBD3D3"
ACCENT_COLOR = "#EC8305"

#
# #TODO: complete check boxes with timeframes 15 min, 1 hr,  2 hr, and 1 day refer to this
# #TODO: create command= to inform decision on what to timeframes to export
#------- variable input ---------#
# class DataFetch(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=BACKGROUND_COLOR)
#         self.controller = controller
#
#         title_font = self.controller.title_font
#
#         label = tk.Label(self, text="Data Extraction", font=title_font)
#         label.grid(row=0, column=1)
#
#         symbol_text = tk.Label(self, text="For which symbol would you \nlike to extract data ", bg=HEADER_COLOR, font=(FONT, 16))
#         symbol_text.grid(row=1, column=0)
#         symbol_entry = Entry(takefocus=1)
#         symbol_entry.grid(row=1, column=1)



        # extract_button = tk.Button(text="Extract Data", bg=ACCENT_COLOR, font=FONT,
        #                            command=lambda: controller.show_frame("DataFetch"))
        # analysis_button = tk.Button(text="Data Analysis",
        #                             bg=ACCENT_COLOR)  # font=FONT, command=lambda: controller.show_frame("DataAnalysis"))
        # correlation_button = tk.Button(text="Create Correlation Matrix", bg=ACCENT_COLOR,
        #                                font=FONT)  # command=lambda, controller,show_frame("CorrelationMatrix")
        #
        # extract_button.grid(row=2, column=0)
        # analysis_button.grid(row=2, column=1)
        # correlation_button.grid(row=2, column=2)

    # function = ""
    # symbol = ""
    # interval = "15min"
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
