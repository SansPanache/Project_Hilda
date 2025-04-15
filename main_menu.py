from tkinter import *
import tkinter as tk
# from tkinter import font as tkfont
# from tkinter import messagebox
# from tkinter import ttk
#
#
# import subprocess
# import os

#------- constants

FONT = "Helvetica"
BACKGROUND_COLOR = "#091057"
HEADER_COLOR = "#024CAA"
BODY_COLOR = "#DBD3D3"
ACCENT_COLOR = "#EC8305"


#----------------   MAIN MENU ------------------------#
class MainMenu(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent, bg=BACKGROUND_COLOR)
		self.controller = controller

		title_font = self.controller.title_font

		label = tk.Label(self, text="Main Menu", font=title_font, bg=BACKGROUND_COLOR)
		label.grid(row=0, column=1)
		sub_label = tk.Label(self, text="What would you like to do?", bg=HEADER_COLOR, font=(FONT, 16))
		sub_label.grid(row=1, column=1)

		extract_button = tk.Button(text="Extract Data", bg=ACCENT_COLOR, font=FONT, command=lambda: controller.show_frame("DataFetch"))
		analysis_button = tk.Button(text="Data Analysis", bg=ACCENT_COLOR) #font=FONT, command=lambda: controller.show_frame("DataAnalysis"))
		correlation_button = tk.Button(text="Create Correlation Matrix", bg=ACCENT_COLOR, font=FONT) #command=lambda, controller,show_frame("CorrelationMatrix")

		extract_button.grid(row=2, column=0)
		analysis_button.grid(row=2, column=1)
		correlation_button.grid(row=2, column=2)

