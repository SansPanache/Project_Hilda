
import tkinter as tk
from tkinter import font as tkfont

from main_menu import MainMenu
from data_fetch import DataFetch
from data_analysis import DataAnalysis
from correlation_matrix import CorrelationMatrix
#------- constants

FONT = "Helvetica"
BACKGROUND_COLOR = "#091057"
HEADER_COLOR = "#024CAA"
BODY_COLOR = "#DBD3D3"
ACCENT_COLOR = "#EC8305"


class AnalysisCommandCenter(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title("Analysis Center")
		self.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)
		self.title_font = tkfont.Font(family=FONT, size=24, weight="bold")

		# Create a canvas as the background
		self.canvas = tk.Canvas(self, bg=BACKGROUND_COLOR, height=600, width=1000)
		self.canvas.grid(row=0, column=0, sticky="nsew")

		# container
		container = tk.Frame(self, bg=BACKGROUND_COLOR)
		container.grid(row=0, column=1)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# Create a canvas widget to serve as the background
		self.canvas = tk.Canvas(container, bg=BACKGROUND_COLOR, width=1000, height=600)
		self.canvas.grid(row=0, column=0, sticky="nsew")





		self.frames = {}
		for F in (MainMenu, DataFetch, DataAnalysis, CorrelationMatrix):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			self.canvas.create_window(0, 0, window=frame, anchor="nw")

		self.show_frame("MainMenu")
#TODO: here I think is the source of my issue.
	def show_frame(self, page_name):
		"""Show a frame for a given page name"""
		frame = self.frames[page_name]
		frame.tkraise()



if __name__ == "__main__":
	app = AnalysisCommandCenter()
	app.mainloop()




