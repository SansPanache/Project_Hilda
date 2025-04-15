import pandas as pd
from numpy.ma.extras import column_stack
from tkinter import *
import tkinter as tk


FONT = "Helvetica"
BACKGROUND_COLOR = "#091057"
HEADER_COLOR = "#024CAA"
BODY_COLOR = "#DBD3D3"
ACCENT_COLOR = "#EC8305"
#
class DataAnalysis(tk.Frame):
		def __init__(self, parent, controller):
			tk.Frame.__init__(self, parent)
			self.controller = controller
			label = tk.Label(self, text="Main Menu", font=controller.title_font)
			sub_label = Label(self, text="What would you like to do?", bg=HEADER_COLOR, font=(FONT, 16))
			label.grid(row=0, column=1)
			sub_label.grid(row=1, column=1)
#--------- gets opening price and shifts it by n rows as requested by user----------#
	# def shifting_opening_price():
	# 	df = pd.read_csv(f"{symbol}_{function}.csv")
	# 	df['open shift'] = df.iloc[:, 2].shift(-{shift})
	# 	df.insert(2, 'open shift', df.pop('open shift'))

#TODO: concatenate all of the csv files into one csv file




#TODO: Functions for: stdiv, factor analysis, logistic regression, forrest, linear regression
#TODO: Correlation matrix option comparing symbols