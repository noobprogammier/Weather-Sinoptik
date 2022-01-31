from tkinter import *
from PIL import Image, ImageTk
class displayweather(object):
	def __init__(self, xroot:str, text:str) -> str:
		self.root = xroot; self.text = text
		lb = Label(self.root, font=("Times New Roman", 8), text=self.text).pack()
def displaygraph(param:str) -> str:
	mn = Tk()
	frame = Frame(mn)
	mn.geometry("%sx%s"%(1920, 1080))
	#frame.grid()
	#lb = Label(frame, text="Weather . . .").pack(pady=20)
	nw = Label(mn, font=("Times New Roman", 35), text="Weather . . .").pack()
	displayweather(xroot=mn, text=param)
	mn.mainloop()