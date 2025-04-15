# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# #from data_fetch import
# import subprocess
# import os
#
# import pandas as pd
#
# #--- Constants---#
# FONT = "Helvetica"
# BACKGROUND_COLOR = "#091057"
# HEADER_COLOR = "#024CAA"
# BODY_COLOR = "#DBD3D3"
# ACCENT_COLOR = "#EC8305"
#
#
#
# #--------------- DATA EXTRACTION ----------------------#
# def data_extract_menu():
# 	extract = Tk()
#
# 	extract.title("Data extractor")
# 	extract.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
# 	canvas = Canvas(width= 1000, height=1000, bg=BODY_COLOR, highlightthickness=0)
# 	canvas.grid(column=0, row=0, columnspan=4, rowspan=4)
#
# 	#TODO: I think I want a  front page where I can choose whether I want to extract or analyse data
# 	#TODO: Need to create a page for data analysis
# #TODO:  Should I have a Menu()? A line up the top with new file exit etc? Seperator()?
#
# 	#-------- Title for data extraction page
# 	symbol_text = Label(text= "Market Data Extraction", bg=BODY_COLOR, font=(FONT, 35))
# 	symbol_text.grid(column=1,row=0, columnspan=2)
#
# 	#---- SYMBOL ENTRY
# 	#TODO: we need to try exception here
# 	symbol_text = Label(text= "Symbol: ", bg=BODY_COLOR, font=(FONT, 16))
# 	symbol_text.grid(column=0,row=1)
# 	symbol_entry = Entry(width=16, font=(FONT, 16))
# 	symbol_entry.grid(column= 1, row=1)
#
# 	#--------- TIME FRAME
# 	#Text
# 	timeframe_select = Label(text = "Timeframe: ",bg=BODY_COLOR, font=(FONT, 16))
# 	timeframe_select.grid(column=0,row=2)
#
# 	#TODO: complete check boxes with timeframes 15 min, 1 hr,  2 hr, and 1 day refer to this
# 	#TODO: create command= to inform decision on what to timeframes to export
# 	#Checkboxes
# 	timeframe_5mins = Checkbutton(text="5 min", bg=BODY_COLOR)
# 	timeframe_5mins.grid(column=1, row=2)
#
# 	#-------- EXPORT OPTIONS
# 	#Text
# 	export_options = Label(text="Format for exporting: ",bg=BODY_COLOR, font=(FONT, 16))
# 	export_options.grid(column=2, row=1)
#
# 	#TODO: create rest of buttons .xls.
# 	#TODO: create command= to trigger exports
# 	#Checkboxes
# 	export_options = Checkbutton(text=".csv", bg=BODY_COLOR)
# 	export_options.grid(column=3, row= 1)
#
# 	back_to_main_menu = Button("Return to main menu", bg=BACKGROUND_COLOR, font=(FONT, 16), command=main_menu)
#
# 	window.mainloop()
# # #-------------- COMMAND EXECUTIONS-----------------------------#
# # def open_csv(filename):
# # 	pass
# #
# #
# # def get_inputs():
# # 	return symbol_entry.get()
# #
# # #TODO: this aint what it ought to be. DEBUG
# # def on_fetch_symbol_data(symbol, FUNCTION_TIME_SERIES, interval):
# # 	symbol = ("AAPL")
# # 	indicators = {"ADX"}
# #
# # 	data = fetch_symbol_price_volume(symbol=symbol, indicators=indicators)
# #
# #
# # 	df = pd.DataFrame(data)
# # 	filename = f"{symbol}_data.csv"
# # 	df.to_csv(filename, index=False)
# #
# # 	if os.path.exists(filename):  # Ensure the file exists
# # 		# Ask the user whether to open the file in the default application
# # 		response = messagebox.askyesno("Open File", f"Do you want to open {filename} in the default application?")
# #
# # 		if response:  # If user clicked Yes
# # 			try:
# # 				# Open the CSV file using the default application for CSV files (Excel, Calc, etc.)
# # 				subprocess.run([filename], check=True)
# # 				print(f"Opened {filename} successfully.")
# # 			except Exception as e:
# # 				print(f"Error opening file: {e}")
# # 		else:
# # 			print(f"{filename} will not be opened.")
# # 	else:
# # 		print(f"File {filename} does not exist.")
# #
# #
# # def on_fetch_indicator_data():
# # 	symbol = "AAPL"
# # 	time_period = "15min"
# #
# # 	data = fetch_indicators_rsi(symbol=symbol, time_period=time_period)
# #
# #
# # 	df = pd.DataFrame(data)
# # 	filename = f"{symbol}_data.csv"
# # 	df.to_csv(filename, index=False)
# #
#
# # ----------------   MAIN MENU ------------------------#
# import tkinter as tk
# from tkinter import font as tkfont
#
#
# class AnalysisCommandCenter(tk.Tk):
# 	def __init__(self):
# 		super().__init__()
# 		self.title("Analysis Center")
# 		self.geometry("600x300")
# 		self.title_font = tkfont.Font(family="Times New Roman", size=16, weight=bold)
#
# 		# container
# 		container = tk.Frame(self)
# 		container.pack(side="top", fill="both", expand="True")
# 		container.grid_rowconfigure(0, weight=1)
# 		container.grid_columnconfigure(0, weight=1)
#
# 		self.frames = {}
# 		for F in (MainMenu, DataExtraction, DataAnalysis, CorrelationMatrix):
# 			pagem_name = F.__name__
# 			frame = F(parent=container, controller=self)
# 			self.frames[page_name] = frame
#
# 			frame.grid(row=0, column=0, )
#
# def main_menu():
# 	window = Tk()
#
# 	window.title("Main menu")
# 	window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
#
# 	input_question = Label(text="What would you like to do?", bg=HEADER_COLOR, font=(FONT, 35))
# 	input_question.grid(column=1, row=0, sticky=N)
#
# 	data_extract = Button(text="Extract data for a symbol", bg=ACCENT_COLOR, font=(FONT, 12), command=data_extract_menu)
# 	data_extract.grid(column=0, row=1, sticky = "e")
#
# 	data_analysis = Button(text="Analyse previous extracted data", bg=ACCENT_COLOR, font=(FONT, 12))
# 	data_analysis.grid(column=1, row=1)
#
# 	correlation_matrix = Button(text="Create a correlation matrix of symbols", bg=ACCENT_COLOR, font=(FONT, 12))
# 	correlation_matrix.grid(column=2, row=1)
#
# 	window.mainloop()
#
# main_menu()
#
