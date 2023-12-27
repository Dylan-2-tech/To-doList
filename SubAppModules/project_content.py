
from customtkinter import CTkButton
from customtkinter import CTkLabel

class project_content():

	def __init__(self, master, content):

		for i in range(len(content)):
			CTkButton (master, text = content[i],
				fg_color = ('black')).grid(row = i, column = 0)